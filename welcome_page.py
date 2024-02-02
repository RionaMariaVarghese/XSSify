# landing_page.py

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()

        combined_text = '''
        <span style='font-size: 150px; color: white; font-style: bold;'>
            WELCOME!
        </span>
        <br>
        <span style='font-size: 50px; color: #2DD096; font-style: bold;'>
           XSSify
        </span>
        '''

        # QLabel with HTML-formatted text
        text_label = QLabel(combined_text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(text_label)

        layout.setContentsMargins(50, 50, 50, 50)


