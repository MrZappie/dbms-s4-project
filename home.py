import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit

from list import ListPage


class HomePage(QWidget):
    def __init__(self,page_stack):
        super().__init__()

        self.page_stack = page_stack
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(main_layout)
        # Centered text
        center_text = QLabel("BookMyTickets")
        center_text.setStyleSheet("font-size:75px; font-weight: bold; color:rgb(255,0,0);")
        center_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addStretch()  # Push text upwards slightly
        main_layout.addWidget(center_text)

        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Search for movies")  # Hint text
        self.search_field.setFixedWidth(300)  # Set fixed width
        self.search_field.setStyleSheet("""
                    QLineEdit {
                        padding: 10px;
                        font-size: 16px;
                        border: 2px solid #ccc;
                        border-radius: 20px;  /* Curved border */
                        background-color: white;
                        color: #000000
                    }
                    QLineEdit:focus {
                        border: 2px solid #ff0000;  /* Red border on focus */
                    }
                """)

        # Create search button with icon
        self.search_button = QPushButton()
        self.search_button.setObjectName("Search_Button_Home")
        self.search_button.setIcon(QIcon.fromTheme("system-search"))  # Add your search icon file
        self.search_button.setFixedWidth(50)
        self.search_button.setStyleSheet("""
                    QPushButton#Search_Button_Home {
                        border-radius: 10px;
                        background-color: rgb(255,0,0);
                        padding: 5px;
                    }
                    QPushButton#Search_Button_Home:hover {
                        background-color: rgb(255,10, 100);
                        border-radius: 10px;
                    }
                """)  # Adjust button size
        self.search_button.clicked.connect(self.on_push_search)
        # Layout to put search field and button together
        layout = QHBoxLayout(self)
        layout.addWidget(self.search_field)
        layout.addWidget(self.search_button) # Space between search field and button
        layout.setContentsMargins(0,0,0,0)
        main_layout.addLayout(layout)
        main_layout.addStretch()

        self.quit_button = QPushButton()
        self.quit_button.setIcon(QIcon.fromTheme("application-exit"))  # Add your search icon file
        self.quit_button.setText("Exit")
        self.quit_button.setFixedWidth(50)
        self.quit_button.setStyleSheet("""
                           QPushButton {
                               border-radius: 10px;
                               background-color: rgb(255,0,0);
                               padding: 5px;
                           }
                           QPushButton:hover {
                               background-color: rgb(255,10, 100);
                               border-radius: 10px;
                           }
                       """)  # Adjust button size
        self.quit_button.clicked.connect(self.on_quit)
        main_layout.addWidget(self.quit_button,alignment=Qt.AlignmentFlag.AlignHCenter)


    def on_push_search(self):
        list_page = ListPage(self.page_stack,self.search_field.displayText())
        self.search_field.setText("")
        self.page_stack.addWidget(list_page)
        self.page_stack.setCurrentWidget(list_page)

    def on_quit(self):
        sys.exit()