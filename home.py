from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from list import ListPage


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('ui/home.ui', self)

        self.search_button.setIcon(QIcon.fromTheme('system-search'))
        self.search_button.clicked.connect(self.on_search_click)

    def on_search_click(self):
        movie_title = self.input.text()
        self.input.setText("")
        self.window().push_page(ListPage(movie_title))

