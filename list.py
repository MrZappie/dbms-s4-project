from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QHBoxLayout, QPushButton, QLineEdit, QSizePolicy,QLabel

from myWidgets.list_widgets import TopBar, DisplayMovies, MovieTile
from movie import MoviePage

class ListPage(QWidget):

    def __init__(self, page_stack, text=None):
        super().__init__()
        self.page_stack = page_stack
        layout = QVBoxLayout(self)

        self.top_bar = TopBar()
        self.display_section = DisplayMovies(text)

        for i in range(12):
            tile = MovieTile(str(i))
            tile.installEventFilter(self)
            tile.clicked.connect(self.on_movie_click)
            self.display_section.add_movie(tile)


        layout.addWidget(self.top_bar, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.display_section, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addStretch()

        self.top_bar.home_button.clicked.connect(self.on_home_click)
        self.top_bar.search_button.clicked.connect(self.on_search_click)

    def eventFilter(self, obj, event):
        return super().eventFilter(obj, event)

    def on_movie_click(self):
        movie_page = MoviePage("Movie Page",self.page_stack)
        self.page_stack.addWidget(movie_page)
        self.page_stack.setCurrentWidget(movie_page)


    def on_home_click(self):
        self.clear_display()
        self.page_stack.removeWidget(self)

    def on_search_click(self):
        self.display_section.display_label.setText("Displaying Movies with Title:"+self.top_bar.search_field.text())

    def clear_display(self):
        """Clears previous movie tiles when switching pages"""
        while self.display_section.grid.count():
            item = self.display_section.grid.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

