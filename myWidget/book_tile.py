from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy


class BookedTile(QWidget):

    def __init__(self,movie,theatre,time,seats):
        super().__init__()

        layout = QHBoxLayout(self)
        label = QLabel(f"Movie: {movie},Theatre: {theatre}, Time: {time}, Seats: {seats}")
        label.setStyleSheet("""
            font-size:15px;
            color: black;
            border: 2px solid #ccc;
            border-radius: 20px;  
        """)
        label.setFixedHeight(50)

        delete = QPushButton()
        delete.setIcon(QIcon.fromTheme("edit-delete"))
        delete.setStyleSheet("""
            background-color: red;
            border-radius: 25px;
        """)
        delete.setFixedSize(50,50)
        layout.addWidget(label)
        #layout.addWidget(delete)