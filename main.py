from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QStackedWidget
from home import HomePage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.account = None
        self.account_books = []

        self.setWindowTitle("Test")
        self.setStyleSheet("background-color:rgb(255,255,255)")
        self.setGeometry(500, 100, 600, 600)
        self.page_stack = QStackedWidget(self)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.page_stack.addWidget(HomePage())
        self.setCentralWidget(self.page_stack)



    def pop_page(self):
        self.page_stack.removeWidget(self.page_stack.currentWidget())

    def push_page(self,page):
        self.page_stack.addWidget(page)
        self.page_stack.setCurrentWidget(page)

    def replace_page(self,page):
        current_widget = self.page_stack.currentWidget()
        self.page_stack.removeWidget(current_widget)

        self.page_stack.addWidget(page)
        self.page_stack.setCurrentWidget(page)

    def book(self,movie,theatre,time,seats):
        self.account_books.append(f"{movie.title}#{theatre.name}#{time}#{seats}")

if __name__ == '__main__':

    app = QApplication([])

    myApp = MainWindow()
    myApp.show()

    app.exec()