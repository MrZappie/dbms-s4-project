from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
import connect

class SignInPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/signin.ui", self)


        self.submit_button.clicked.connect(self.on_submit_click)
        self.back_button.clicked.connect(self.on_back_click)
        self.login_button.clicked.connect(self.on_log_in_click)

    def on_submit_click(self):
        username = self.username.text()
        password = self.password.text()
        c_password = self.confirm_password.text()

        if username in self.window().real_list.keys():
            QMessageBox.information(self, "User Already Present", "Need another name")
            return

        if not username or not password or not c_password:
            QMessageBox.information(self, "Unfilled Fields", "All Fields must be filled")
            return

        if password != c_password:
            QMessageBox.information(self, "Unmatched Password", "Password And Confirm Password doesn't Match")
            return

        self.window().account = username
        self.window().real_list[username] = password

        self.window().cursor.execute(f"insert into user(username, password) values ('{username}','{c_password}')")
        self.window().con.commit()

        self.on_back_click()

    def on_log_in_click(self):
        from login import LoginPage
        self.window().replace_page(LoginPage())

    def on_back_click(self):
        self.window().pop_page()