from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class HelpPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("This is the Help Page")
        label.setStyleSheet("font-size: 24px;")
        layout.addWidget(label)
