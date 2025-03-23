from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6 import uic

from myWidget.theatre_tile import TheatreTile
from seats import SeatPage


class ShowsPage(QWidget):

    def __init__(self,movie):
        super().__init__()
        uic.loadUi("ui/shows.ui",self)

        self.title.setText("Title: "+movie.title)
        self.movie = movie

        if not self.scrollAreaWidgetContents.layout():
            self.scrollAreaWidgetContents.setLayout(QVBoxLayout())

        self.back_button.clicked.connect(self.on_back_click)

    def showEvent(self, a0):
        try:
            self.window().cursor.execute(f"select * from movies where title like '%{self.movie.title}%'")
            result = self.window().cursor.fetchall()
            id, _, description, date, duration, theme, rating = result[0]

            self.description.setText("Description: " + description)
            self.date.setText("Released on: " + str(date))
            self.theme.setText("Theme: " + theme)
            self.duration.setText("Duration (minutes): " + str(duration))
            self.rating.setText("Ratings: " + str(rating))

            self.window().cursor.execute(f"select * from shows where movie_id = {id}")
            result = self.window().cursor.fetchall()

            if len(result) != 0:
                for i in range(len(result)):
                     name = result[i][2]
                     date_time = str(result[i][3]) + " -- " + str(result[i][4])
                     self.add_theatre(TheatreTile(name, [date_time], self.movie))
            else:
                label = QLabel("No shows available")
                label.setStyleSheet("""
                        background-color: white;
                        color: black;
                        font-size: 35px;
                """)
                self.scrollAreaWidgetContents.layout().addWidget(label)


        except Exception as e:
            print(f"{e}")

        super().showEvent(a0)

    def on_back_click(self):
        self.window().pop_page()

    def add_theatre(self,theatre):
        for i in theatre.shows_button:
            i.clicked.connect(lambda _,b=i: self.on_time_click(theatre,b))
        self.scrollAreaWidgetContents.layout().addWidget(theatre,Qt.AlignmentFlag.AlignLeft)

    def clear_grid(self):
        while self.scrollAreaWidgetContents.layout().count():
            item = self.scrollAreaWidgetContents.layout().takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def on_time_click(self,theatre,button):
        self.clear_grid()
        self.window().push_page(SeatPage(theatre,button.text(),self.movie))