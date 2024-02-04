from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("This is the Profile Page")
        layout.addWidget(label)
