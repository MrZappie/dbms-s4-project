from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

import connect
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


        try:
            self.window().cursor.execute(f"select * from user where username = '{username}'")
            result = self.window().cursor.fetchone()

            if result is None:
                self.show_message_box("User Not Present", "Incorrect Username")
                return

            db_username, db_password = result[0], result[1]

            if db_password != password:
                self.show_message_box("Incorrect Password or Username", "Please Recheck")
                return

            # Login successful
            self.window().account = username
            self.on_back_click()

        except Exception as e:
            print(f"Database error: {e}")
            self.show_message_box("Error", "An error occurred while accessing the database.")

    def on_sign_in_click(self):
        self.window().replace_page(SignInPage())

    def on_back_click(self):
        self.window().pop_page()

    def show_message_box(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.exec()