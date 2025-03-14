import os

from PyQt6.QtGui import QIcon, QPainter, QLinearGradient, QColor, QBrush, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QScrollArea
from PyQt6.QtCore import Qt, QRect

from myWidgets.movie_widgets import HomeTitle, SeatArea, SeatButton


class MoviePage(QWidget):

    def __init__(self,movie,page_stack):
        super().__init__()
        self.page_stack = page_stack
        layout = QVBoxLayout(self)



        back_button = QPushButton()
        back_button.setText("Back")
        back_button.setMinimumSize(50,50)
        back_button.setStyleSheet("""
                    QPushButton {
                        border-radius: 10px;
                        color: black;
                        background-color: rgb(255,255,255);
                    }
                    QPushButton:hover {
                        background-color: rgb(0,0, 0);
                        color: white;
                        border-radius: 10px;
                    }""")
        back_button.clicked.connect(self.on_back)

        home_title = HomeTitle()
        seat_area = SeatArea()

        for i in range(1,61):
            seat_area.add_seat(SeatButton(str(i)))
        layout.addWidget(back_button,alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(home_title)
        layout.addWidget(seat_area)
        layout.addWidget(QPushButton("Book"))

    def on_back(self):
        self.page_stack.removeWidget(self)

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(255, 100, 100))  # Light Red
        gradient.setColorAt(1, QColor(200, 0, 0))  # Dark Red
        painter.fillRect(self.rect(), QBrush(gradient))