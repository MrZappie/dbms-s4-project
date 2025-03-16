from PyQt6.QtWidgets import QWidget
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
        self.window().account = self.username.text()
        self.on_back_click()

    def on_sign_in_click(self):
        self.window().replace_page(SignInPage())

    def on_back_click(self):
        self.window().pop_page()