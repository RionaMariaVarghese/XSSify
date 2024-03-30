import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

class TutorialPage(QWidget):
    returnToIndexSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        # State variables
        self.page_state = "initial"  # Initial page state

        # Main layout for the entire page
        main_layout = QVBoxLayout(self)

        # Top layout containing the hamburger menu
        top_layout = QHBoxLayout()
        self.setup_index_button(top_layout)
        main_layout.addLayout(top_layout)

        # Scroll Area for the content
        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("border: none; background-color: #252839;")
        scroll_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(scroll_area)

        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)
        inner_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_area.setWidget(inner_widget)
        scroll_area.setWidgetResizable(True)

        # Content layout
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        inner_layout.addWidget(self.content_widget)

        # Bottom layout containing navigation buttons
        self.bottom_layout = QHBoxLayout()
        main_layout.addLayout(self.bottom_layout)

        self.setLayout(main_layout)

        # Initialize the current page
        self.show_initial_page()

    def setup_index_button(self, layout):
        index_button = QPushButton("☰")
        index_button.clicked.connect(self.emit_return_to_index_signal)
        index_button.setStyleSheet(
            """
                QPushButton {
                    font-size: 25px;
                    background-color: rgba(0, 0, 0, 0);
                    color: #2DD096;
                    padding: 2px 25px;
                    border-radius: 5px;
                }
                
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }
                
                QPushButton:pressed {
                    background-color: rgba(255, 255, 255, 0.2);
                }
            """
        )
        layout.addWidget(index_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def show_initial_page(self):
        # Clear existing content and buttons
        self.clear_layout(self.content_layout)
        self.clear_layout(self.bottom_layout)

        # Add content to the initial page
        label = QLabel("This is the Tutorials Page")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(label)

        # Add the continue button
        btn_cont = QPushButton("Continue")
        btn_cont.clicked.connect(self.show_intro_page)
        self.bottom_layout.addWidget(btn_cont)

    def show_intro_page(self):
        # Clear existing content and buttons
        self.clear_layout(self.content_layout)
        self.clear_layout(self.bottom_layout)

        # Set the page state to "intro"
        self.page_state = "intro"

        # Content and layout for the introduction page
        heading = QLabel("INTRODUCTION")
        heading.setStyleSheet("font-size: 36px; color: #2DD096; font-weight: bold; text-decoration: underline;")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        content = QLabel("""
        Cross-Site Scripting (XSS) is a vulnerability in web applications that allows attackers to inject malicious scripts into web pages viewed by other users.<br><br>
        XSS attacks can lead to various consequences, including data theft, session hijacking, defacement, and malware distribution.<br><br>
        This tutorial aims to introduce beginners to XSS, exploitation, commonly used apps vulnerable to XSS, and preventive measures to mitigate this threat.
        """)
        content.setStyleSheet("font-size: 24px; color: white; font-weight: regular; text-align: justify;")
        content.setAlignment(Qt.AlignmentFlag.AlignLeft)
        content.setWordWrap(True)

        # Add content and buttons to the introduction page
        self.content_layout.addWidget(heading)
        self.content_layout.addWidget(content)

        # Add navigation buttons
        self.add_navigation_buttons()

    def show_understanding_page(self):
        # Clear existing content and buttons
        self.clear_layout(self.content_layout)
        self.clear_layout(self.bottom_layout)

        # Set the page state to "understanding"
        self.page_state = "understanding"

        # Content and layout for the understanding page
        heading = QLabel("UNDERSTANDING")
        heading.setStyleSheet("font-size: 36px; color: #2DD096; font-weight: bold; text-decoration: underline;")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        content = QLabel("""
        XSS occurs when an attacker injects malicious scripts into web applications, which are then executed in the browsers of unsuspecting users.<br><br>
        There are three main types of XSS:<br>
        - Reflected XSS: The injected script is reflected off a web server and executed in the user's browser.<br>
        - Stored XSS: The injected script is stored on the server and executed whenever a user accesses the affected page.<br>
        - DOM-based XSS: The payload is injected into the DOM (Document Object Model) and executed in the victim's browser.
        """)
        content.setStyleSheet("font-size: 24px; color: white; font-weight: regular; text-align: justify;")
        content.setAlignment(Qt.AlignmentFlag.AlignLeft)
        content.setWordWrap(True)

        # Add content and buttons to the understanding page
        self.content_layout.addWidget(heading)
        self.content_layout.addWidget(content)

        # Add navigation buttons
        self.add_navigation_buttons()

    def add_navigation_buttons(self):
        # Clear existing navigation buttons
        self.clear_layout(self.bottom_layout)

        # Add previous button
        if self.page_state != "initial":
            btn_prev = QPushButton("Previous")
            btn_prev.clicked.connect(self.show_previous_page)
            self.bottom_layout.addWidget(btn_prev)

        # Add next button
        btn_next = QPushButton("Next")
        btn_next.clicked.connect(self.show_next_page)
        self.bottom_layout.addWidget(btn_next)

    def show_previous_page(self):
        if self.page_state == "understanding":
            self.show_intro_page()

    def show_next_page(self):
        if self.page_state == "intro":
            self.show_understanding_page()

    def clear_layout(self, layout):
        # Clear the layout by removing all widgets
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Tutorial Page")
#         self.setGeometry(100, 100, 800, 600)

#         tutorial_page = TutorialPage()
#         tutorial_page.returnToIndexSignal.connect(self.return_to_index_page)

#         self.setCentralWidget(tutorial_page)

#     def return_to_index_page(self):
#         print("Returning to index page")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
