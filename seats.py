from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QMessageBox
from PyQt6 import uic

from myWidget.seat_tile import SeatTile


class SeatPage(QWidget):

    def __init__(self,theatre,time,movie):
        super().__init__()
        uic.loadUi("ui/seats.ui",self)
        self.x,self.y = 0,0
        self.movie,self.theatre,self.time = movie,theatre,time
        self.details.setText(f"Movie: {movie.title}, Theatre: {theatre.name}, Time: {time}")
        self.seat_buttons = []

        self.back_button.clicked.connect(self.on_back_click)
        self.book_button.clicked.connect(self.on_book_click)

        self.grid = QGridLayout()
        self.scrollAreaWidget.setLayout(self.grid)


    def showEvent(self, a0):
        try:
            self.window().cursor.execute(f"select seat_name from seats where theatre_name = '{self.theatre.name}'")
            result = self.window().cursor.fetchall()
            print(result)
            for i in range(0, 60):
                seat_name = chr((i//10)+65) + str((i%10)+1)

                booked = False
                for i in result:
                    if seat_name in i:
                        booked = True

                seat = SeatTile(str(seat_name),booked)
                self.seat_buttons.append(seat)
                self.add_button(seat)
        except Exception as e:
            print(f"Error: {e}")
        super().showEvent(a0)


    def on_book_click(self):
        if self.window().account is None:
            msg = QMessageBox()
            msg.setWindowTitle("No User")
            msg.setText("Must Be Logged In")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
        else:
            #backend
            seats = []
            for i in self.seat_buttons:
                if i.isChecked():
                    seats.append(i.text())
                    try:
                        self.window().cursor.execute(f"insert into seats(seat_name,movie_name,theatre_name,time,account) values('{i.text()}','{self.movie.title}','{self.theatre.name}','{self.time}','{self.window().account}')")
                        self.window().con.commit()

                    except Exception as e:
                        print(f"{e}")

            self.window().book(self.movie,self.theatre,self.time,seats)

            self.on_back_click()


    def on_back_click(self):
        self.window().pop_page()



    def add_button(self,seat):
        self.grid.addWidget(seat,self.y, self.x,alignment=Qt.AlignmentFlag.AlignLeft)
        self.x += 1
        if self.x>=10:
            self.y+=1
            self.x = 0