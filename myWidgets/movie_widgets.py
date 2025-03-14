from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QScrollArea, QGridLayout, QCheckBox, QPushButton


class HomeTitle(QWidget):

    def __init__(self):
        super().__init__()
        self.movie_stuff = QHBoxLayout(self)

        self.movie_image = QPixmap("images/no_image.jpg")
        self.movie_image = self.movie_image.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

        image_label = QLabel()
        image_label.setMaximumSize(200, 200)
        image_label.setPixmap(self.movie_image)
        image_label.setStyleSheet("border-radius:50px;")
        self.movie_stuff.addWidget(image_label, alignment=Qt.AlignmentFlag.AlignTop)

        title = QLabel(" MOVIE - TITLE")
        title.setStyleSheet("color: white;background: transparent;font-size: 55px")

        self.movie_stuff.addWidget(title,alignment=Qt.AlignmentFlag.AlignTop)


class SeatArea(QWidget):
    def __init__(self):
        super().__init__()
        self.x,self.y = 0,0
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: rgb(230,230,230);border-radius:10px")

        self.scroll = QScrollArea()
        self.scroll.setMinimumHeight(400)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)

        self.widget = QWidget()
        self.grid = QGridLayout()
        self.grid.setContentsMargins(5, 0, 0, 10)
        self.grid.setSpacing(5)
        self.widget.setLayout(self.grid)
        self.scroll.setWidget(self.widget)
        layout.addWidget(self.scroll)

    def add_seat(self, seat):
        self.grid.addWidget(seat, self.y, self.x)
        self.x += 1
        if self.x >= 10:
            self.y += 1
            self.x = 0


class SeatButton(QCheckBox):

    def __init__(self,number):
        super().__init__()
        self.setMinimumSize(50,50)
        self.setStyleSheet("""
            background-color: red;
            color:white;
            font-size: 20px;
            border-radius: 20px;
        """)
        self.setText(number)