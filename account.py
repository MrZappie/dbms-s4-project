from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from PyQt6 import uic

from myWidget.book_tile import BookedTile
from myWidget.seat_tile import SeatTile


class AccountPage(QWidget):

    def __init__(self):
        super().__init__()
        self.x = 0
        uic.loadUi("ui/account.ui",self)

        self.back_button.clicked.connect(self.on_back_click)
        self.logout_button.clicked.connect(self.on_logout_click)

        self.sc_layout = QGridLayout()
        self.scrollAreaWidgetContents.setLayout(self.sc_layout)



    def showEvent(self, event):
        super().showEvent(event)

        if self.window():
            for i in self.window().account_books:
                movie, theatre, title, seat = i.split("#")
                book_tile = BookedTile(movie,theatre,title,seat)
                self.sc_layout.addWidget(book_tile,self.x,0,alignment=Qt.AlignmentFlag.AlignLeft)
                self.x+=1
        else:
            print("MainWindow not found.")

    def clear_grid(self):
        while self.sc_layout.count():
            item = self.sc_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.x = 0

    def on_logout_click(self):
        self.window().account = None
        self.on_back_click()

    def on_back_click(self):
        self.clear_grid()
        self.window().pop_page()