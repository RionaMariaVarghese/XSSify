from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import pyqtSignal, Qt

class ProfilePage(QWidget):
    returnToIndexSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        ham_layout = QHBoxLayout()
        ham_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)  # Align to top-left
        layout.addLayout(ham_layout)

        btn_return = QPushButton("☰")
        btn_return.clicked.connect(self.emit_return_to_index_signal)
        btn_return.setStyleSheet("font-size: 15px; color: #2DD096;")
        ham_layout.addWidget(btn_return)

        label_profile = QLabel("PROFILE")
        label_profile.setStyleSheet("font-size: 20px; color: white; padding-left: 5px;")
        ham_layout.addWidget(label_profile)

        label = QLabel("This is the Profile Page")
        layout.addWidget(label)

        self.setLayout(layout)

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()
