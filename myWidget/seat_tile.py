from PyQt6.QtWidgets import QPushButton

class SeatTile(QPushButton):

    def __init__(self, name, booked=False):
        super().__init__()
        self.setText(name)
        self.setFixedSize(100, 50)

        if not booked:
            self.setCheckable(True)
            self.update_style(self.isChecked())  # Initialize style

            self.toggled.connect(self.update_style)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: black;
                    color: white;
                    font-size: 16px;
                    padding: 10px;
                    border-radius: 5px;
                }
            """)

    def update_style(self, checked):
        if checked:
            self.setStyleSheet("""
                QPushButton {
                    background-color: green;
                    color: white;
                    font-size: 10px;
                    border-radius: 5px;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: red;
                    font-size: 10px;
                    border-radius: 5px;
                }
            """)
