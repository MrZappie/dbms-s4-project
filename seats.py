from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QMessageBox
from PyQt6 import uic

from myWidget.seat_tile import SeatTile


class SeatPage(QWidget):

    def __init__(self,theatre,time,movie):
        super().__init__()
        uic.loadUi("ui/seats.ui",self)
        self.x,self.y = 0,0
        self.movie,self.theatre,self.time = movie,theatre,time
        self.details.setText(f"Movie: {movie.title}, Theatre: {theatre.name}, Time: {time}")
        self.seat_buttons = []

        self.back_button.clicked.connect(self.on_back_click)
        self.book_button.clicked.connect(self.on_book_click)

        self.grid = QGridLayout()
        self.scrollAreaWidget.setLayout(self.grid)

        for i in range(1,61):
            seat = SeatTile(str(i))
            self.seat_buttons.append(seat)
            self.add_button(seat)


    def on_book_click(self):
        if self.window().account is None:
            msg = QMessageBox()
            msg.setWindowTitle("No User")
            msg.setText("Must Be Logged In")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
        else:
            #backend
            seats = []
            for i in self.seat_buttons:
                if i.isChecked():
                    seats.append(i.text())

            self.window().book(self.movie,self.theatre,self.time,seats)

            self.on_back_click()


    def on_back_click(self):
        self.window().pop_page()



    def add_button(self,seat):
        self.grid.addWidget(seat,self.y, self.x,alignment=Qt.AlignmentFlag.AlignLeft)
        self.x += 1
        if self.x>=10:
            self.y+=1
            self.x = 0