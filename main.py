import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton
from home import HomePage


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color:rgb(255,255,255)")
        self.setGeometry(500, 100, 600, 600)
        self.page_stack = QStackedWidget(self)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.page_stack.addWidget(HomePage(self.page_stack))
        layout = QVBoxLayout(self)

        layout.addWidget(self.page_stack)





if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
