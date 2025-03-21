from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

from signin import SignInPage


class LoginPage(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui",self)

        self.submit_button.clicked.connect(self.on_submit_click)
        self.back_button.clicked.connect(self.on_back_click)
        self.sign_in_button.clicked.connect(self.on_sign_in_click)

    def on_submit_click(self):
        username = self.username.text()
        password = self.password.text()

        if username not in self.window().real_list.keys():
            msg = QMessageBox()
            msg.setWindowTitle("User Not Present")
            msg.setText("Incorrect Username")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
            return

        if self.window().real_list[username] != password:
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect Password or Username")
            msg.setText("Please Recheck")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
            return



        self.window().account = username
        self.window().account_books = self.window().booked[username]
        self.on_back_click()

    def on_sign_in_click(self):
        self.window().replace_page(SignInPage())

    def on_back_click(self):
        self.window().pop_page()