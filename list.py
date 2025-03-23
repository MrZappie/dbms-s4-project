from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QGridLayout, QScrollArea

from account import AccountPage
from login import LoginPage
from myWidget.movie_tile import MovieTile
from shows import ShowsPage

display_title_text = "Displaying Movies with Title Containing Words: "

class ListPage(QWidget):

    def __init__(self,movie_title):
        super().__init__()
        uic.loadUi('ui/list.ui', self)

        self.x ,self.y = 0,0

        self.home_button.setIcon(QIcon.fromTheme("go-home"))
        self.input.setText(movie_title)
        self.display_title.setText(display_title_text+movie_title)
        self.search_button.setIcon(QIcon.fromTheme('system-search'))


        self.scroll = QScrollArea()
        self.scroll.setMinimumHeight(600)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setWidgetResizable(True)

        self.widget = QWidget()
        self.grid = QGridLayout()
        self.grid.setContentsMargins(0, 2, 3, 0)
        self.grid.setSpacing(10)
        self.widget.setLayout(self.grid)
        self.scroll.setWidget(self.widget)


        self.layout().addWidget(self.scroll)

        self.home_button.clicked.connect(self.on_home_click)
        self.search_button.clicked.connect(self.on_search_click)
        self.account_button.clicked.connect(self.on_account_click)


    def on_account_click(self):
        if self.window().account is None:
            self.window().push_page(LoginPage())
        else:
            self.window().push_page(AccountPage())

    def on_search_click(self):
        movie_title = self.input.text()
        self.display_title.setText(display_title_text+movie_title)
        self.clear_grid()

        #backend
        if movie_title is None:
            movie_title = ""
        try:
            self.window().cursor.execute(f"select title from movies where title like '%{movie_title}%'")
            result = self.window().cursor.fetchall()
            for i in result:
                self.add_movie(MovieTile(i[0]))

        except Exception as e:
            print(f"{e}")



    def on_movie_click(self, movie):
        self.window().push_page(ShowsPage(movie))

    def on_home_click(self):
        self.window().pop_page()

    def clear_grid(self):
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.x, self.y = 0, 0


    def showEvent(self, event):
        movie_title = self.input.text()
        if movie_title is None:
            movie_title = ""
        try:
            self.window().cursor.execute(f"select title from movies where title like '%{movie_title}%'")
            result = self.window().cursor.fetchall()
            for i in result:
                self.add_movie(MovieTile(i[0]))
        except Exception as e:
            print(f"{e}")


        if self.window().account is not None:
            self.account_button.setText(self.window().account)
        else:
            self.account_button.setText("Not Logged in")
        super().showEvent(event)

    def add_movie(self, movie):
        movie.clicked.connect(lambda: self.on_movie_click(movie))
        self.grid.addWidget(movie, self.y, self.x,alignment=Qt.AlignmentFlag.AlignLeft)
        self.x += 1
        if self.x>8:
            self.y+=1
            self.x = 0