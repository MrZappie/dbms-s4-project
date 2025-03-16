from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class TheatreTile(QWidget):

    def __init__(self,name,shows,movie):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(10)
        self.name = name
        self.shows = shows

        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 10px;
            }
        """)
        self.setMinimumSize(500,100)

        self.name_label = QLabel("Name: "+self.name)
        self.name_label.setMaximumSize(300,50)
        self.name_label.setStyleSheet("""
            padding: 10px;
            color: red;
            font-size: 15px;
        """)

        layout.addWidget(self.name_label,alignment=Qt.AlignmentFlag.AlignLeft)

        self.shows_button = []
        for i in range(len(shows)):
            button = QPushButton(shows[i])
            button.setFixedSize(100,50)
            button.setStyleSheet("""
                QPushButton{
                    background-color: white;
                    color: red;
                    border-radius: 10px;
                }
                QPushButton:hover{
                    background-color: black;
                    color: white;
                }
            """)
            self.shows_button.append(button)
            layout.addWidget(button,alignment= Qt.AlignmentFlag.AlignLeft)

        layout.addStretch()

