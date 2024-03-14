from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()

        # Content and layout
        combined_text = '''
        <span style='font-size: 150px; color: white; font-weight: bold;'>
            XSSify
        </span>
        <br>
        <span style='font-size: 50px; color: #2DD096; font-weight: bold;'>
           Beginner's Guide to XSS Exploitation
        </span>
        '''

        text_label = QLabel(combined_text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(text_label)

        layout.setContentsMargins(50, 50, 50, 50)


