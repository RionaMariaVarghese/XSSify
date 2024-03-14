from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import pyqtSignal, Qt

class ProfilePage(QWidget):
    returnToIndexSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("This is the Tutorials Page")
        layout.addWidget(label)

        # Button to return to index page
        btn_return = QPushButton("Return to Index Page")
        btn_return.clicked.connect(self.emit_return_to_index_signal)
        layout.addWidget(btn_return)

        self.setLayout(layout)

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()
