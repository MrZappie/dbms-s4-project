from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic



class SignInPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/signin.ui",self)

        self.submit_button.clicked.connect(self.on_submit_click)
        self.back_button.clicked.connect(self.on_back_click)
        self.login_button.clicked.connect(self.on_log_in_click)


    def on_submit_click(self):
        username = self.username.text()
        password = self.password.text()
        c_password = self.confirm_password.text()

        if username in self.window().real_list.keys():
            msg = QMessageBox()
            msg.setWindowTitle("User Already Present")
            msg.setText("Need another name")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
            return

        if not username or not password or not c_password:
            msg = QMessageBox()
            msg.setWindowTitle("Unfilled Fields")
            msg.setText("All Fields must be filled")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
            return

        if password != c_password:
            msg = QMessageBox()
            msg.setWindowTitle("Unmatched Password")
            msg.setText("Password And Confirm Password doesn't Match ")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
            return



        self.window().account = username
        self.window().real_list[username] = password
        self.on_back_click()

    def on_log_in_click(self):
        from login import LoginPage
        self.window().replace_page(LoginPage())

    def on_back_click(self):
        self.window().pop_page()
