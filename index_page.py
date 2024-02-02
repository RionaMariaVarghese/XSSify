from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class IndexPage(QWidget):
    def __init__(self):
        super().__init__()

        # Index page content
        index_label = QLabel("This is the Index Page", self)
        index_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Arrow icon
        arrow_icon = QLabel(self)
        arrow_icon.setPixmap(QIcon.fromTheme("go-next").pixmap(32, 32))  # Example: Using a built-in Qt arrow icon

        # Layout setup
        layout = QVBoxLayout(self)

        # Horizontal layout for label and icon
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(index_label)
        horizontal_layout.addWidget(arrow_icon)
        horizontal_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the horizontal layout to the main vertical layout
        layout.addLayout(horizontal_layout)
