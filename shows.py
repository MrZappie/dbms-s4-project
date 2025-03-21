from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
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

        #backend
        for i in range(3):
            self.add_theatre(TheatreTile(str(i),['1:00 AM','10:30 AM','3:00 PM'],movie))


    def on_back_click(self):
        self.window().pop_page()

    def add_theatre(self,theatre):
        for i in theatre.shows_button:
            i.clicked.connect(lambda _,b=i: self.on_time_click(theatre,b))
        self.scrollAreaWidgetContents.layout().addWidget(theatre,Qt.AlignmentFlag.AlignLeft)

    def on_time_click(self,theatre,button):
        self.window().push_page(SeatPage(theatre,button.text(),self.movie))