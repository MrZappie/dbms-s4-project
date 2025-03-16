from PyQt6.QtWidgets import QWidget
from PyQt6 import uic



class SignInPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/signin.ui",self)

        self.submit_button.clicked.connect(self.on_submit_click)
        self.back_button.clicked.connect(self.on_back_click)
        self.login_button.clicked.connect(self.on_log_in_click)


    def on_submit_click(self):
        self.window().account = self.username.text()
        self.on_back_click()

    def on_log_in_click(self):
        from login import LoginPage
        self.window().replace_page(LoginPage())

    def on_back_click(self):
        self.window().pop_page()
