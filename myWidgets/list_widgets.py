from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QSize, QEasingCurve
from PyQt6.QtGui import QPainter, QLinearGradient, QColor, QBrush
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QLineEdit, QGridLayout, \
    QStackedWidget, QScrollArea, QSizePolicy


class DisplayMovies(QWidget):

    def __init__(self, text = None):
        super().__init__()
        self.x , self.y = 0,0
        layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: rgb(230,230,230);border-radius:10px")
        if text is None:
            text = "#Not Selected"
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.display_label = QLabel("Displaying Movies with Title: " + text)
        self.display_label.setStyleSheet("""
                    font-size: 24px;
                    color: black;
        """)
        layout.addWidget(self.display_label)

        self.scroll = QScrollArea()
        self.scroll.setMinimumHeight(600)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)


        self.widget = QWidget()
        self.grid = QGridLayout()
        self.grid.setContentsMargins(0,2,3,0)
        self.grid.setSpacing(10)
        self.widget.setLayout(self.grid)
        self.scroll.setWidget(self.widget)
        layout.addWidget(self.scroll,stretch=1)


    def add_movie(self, movie):
        self.grid.addWidget(movie, self.y, self.x,alignment=Qt.AlignmentFlag.AlignLeft)
        self.x += 1
        if self.x>8:
            self.y+=1
            self.x = 0

class TopBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: transparent;")

        # Create layout for top bar
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Home Button (Icon on Left)
        self.home_button = QPushButton()
        self.home_button.setIcon(QIcon.fromTheme("user-home"))  # Replace with your actual icon
        self.home_button.setStyleSheet("""
                    QPushButton {
                        border-radius: 10px;
                        background-color: rgb(255,0,0);
                    }
                    QPushButton:hover {
                        background-color: rgb(255,10, 100);
                        border-radius: 10px;
                    }""")
        self.home_button.setFixedSize(60, 60)  # Set button size

        # Search Bar (With Search Icon)
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Search for movies")
        self.search_field.setStyleSheet("""
            QLineEdit {
                padding: 15px 15px;
                font-size: 16px;
                border: 2px solid #555;
                border-radius: 20px;
                background-color: rgba(0,0,0,0.1);
                color: black;
            }
        """)
        self.search_field.setFixedWidth(300)  # Adjust width

        self.search_button = QPushButton()
        self.search_button.setIcon(QIcon.fromTheme("system-search"))  # Add your search icon file
        self.search_button.setFixedWidth(50)
        self.search_button.setStyleSheet("""
                            QPushButton {
                                border-radius: 10px;
                                background-color: rgb(255,0,0);
                                padding: 5px;
                            }
                            QPushButton:hover {
                                background-color: rgb(255,10, 100);
                                border-radius: 10px;
                            }
                        """)

        # Circular Button on the Right (Profile/Icon)
        self.circle_button = QPushButton()
        self.circle_button.setStyleSheet("""
            QPushButton {
                background-color: red;
                border-radius: 15px;  /* Circular button */
                width: 30px;
                height: 30px;
            }
        """)
        self.circle_button.setFixedSize(30, 30)

        # Add widgets to layout
        layout.addWidget(self.home_button, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.search_field, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.search_button)
        layout.addStretch()  # Pushes the circular button to the right
        layout.addWidget(self.circle_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)



class MovieTile(QPushButton):
    def __init__(self, title=None):
        super().__init__()

        # Define sizes
        self.original_size = QSize(150, 175)
        self.expanded_size = QSize(170, 235)

        self.setFixedSize(self.original_size)  # Set initial size

        self.setStyleSheet("""
             QPushButton {
                border-radius: 10px;
                background-color: rgb(150,150,150);
                color: black;
                padding: 5px;
             }
        """)
        self.setText(title)

        # Initialize animations
        self.anim = QPropertyAnimation(self, b"minimumSize")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)

    def enterEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(self.size())
        self.anim.setEndValue(self.expanded_size)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(self.size())
        self.anim.setEndValue(self.original_size)
        self.anim.start()
        super().leaveEvent(event)