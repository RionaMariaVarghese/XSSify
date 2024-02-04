from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class TutorialPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("This is the Tutorials Page")
        layout.addWidget(label)
