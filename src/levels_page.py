from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class LevelsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("This is the Levels Page")
        layout.addWidget(label)
