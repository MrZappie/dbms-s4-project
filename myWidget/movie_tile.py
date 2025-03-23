import random

from PyQt6.QtCore import QSize, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPushButton


class MovieTile(QPushButton):
    def __init__(self, title=None):
        super().__init__()
        self.title = title
        # Define sizes
        self.original_size = QSize(150, 175)
        self.expanded_size = QSize(170, 235)

        self.setFixedSize(self.original_size)  # Set initial size

        self.setStyleSheet(f"""
             QPushButton {{
                border-radius: 10px;
                background-color: {self.generate_light_color()};
                color: black;
                padding: 5px;
             }}
        """)
        self.setText(self.title)

        # Initialize animations
        self.anim = QPropertyAnimation(self, b"minimumSize")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)

    def enterEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(self.size())
        self.anim.setEndValue(self.expanded_size)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(self.size())
        self.anim.setEndValue(self.original_size)
        self.anim.start()
        super().leaveEvent(event)

    def generate_light_color(self):
        red = random.randint(150, 255)
        green = random.randint(150, 255)
        blue = random.randint(150, 255)
        return QColor(red, green, blue).name()