from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel


class BookedTile(QWidget):

    def __init__(self,movie,theatre,time,seats):
        super().__init__()

        layout = QHBoxLayout(self)
        label = QLabel(f"{movie},{theatre},{time},{seats}")
        label.setStyleSheet("""
            font-size:25px;
            color: black;
        """)
        layout.addWidget(label)