from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from PyQt6 import uic

from myWidget.book_tile import BookedTile



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
        #backend
        self.username.setText("Username: "+self.window().account)

        seats_d ={}

        if self.window():
            try:
                self.window().cursor.execute(f"select * from seats where account = '{self.window().account}'")
                result = self.window().cursor.fetchall()
                for i in result:
                    seat,movie,theatre,time = i[1:5]
                    if movie+'#'+theatre+'#'+time in seats_d.keys():
                        seats_d[movie+'#'+theatre+'#'+time].append(seat)
                    else:
                        seats_d[movie+'#'+theatre+'#'+time] = [seat,]
            except Exception as e:
                print(f"Error: {e}")

            for i in seats_d:
                movie, theatre, title = i.split("#")
                seat = seats_d[i]
                book_tile = BookedTile(movie,theatre,title,str(seat))
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
        self.window().account_books = []
        self.on_back_click()

    def on_back_click(self):
        self.clear_grid()
        self.window().pop_page()