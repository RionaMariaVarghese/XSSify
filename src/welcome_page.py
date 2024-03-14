from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

class WelcomePage(QWidget):
    returnToIndexSignal = pyqtSignal()
    def __init__(self):
        super().__init__()

        # Content and layout
        combined_text = '''
        <span style='font-size: 100px; color: #2DD096; font-weight: bold;'>
            XSSify
        </span>
        <br>
        <span style='font-size: 20px; color: white; font-weight: regular;'>
           Beginner's Guide to XSS Exploitation
        </span>
        '''

        text_label = QLabel(combined_text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(text_label)

        # layout.setContentsMargins(50, 50, 50, 50)

        arrow_button = QPushButton("▼")
        arrow_button.setStyleSheet("font-size: 20px; color: #2DD096;")
        arrow_button.clicked.connect(self.emit_navigate_to_index_signal)
        arrow_layout = QHBoxLayout()
        arrow_layout.addStretch()
        arrow_layout.addWidget(arrow_button, alignment=Qt.AlignmentFlag.AlignCenter)
        arrow_layout.addStretch()
        layout.addLayout(arrow_layout)

    def emit_navigate_to_index_signal(self):
        self.returnToIndexSignal.emit()


