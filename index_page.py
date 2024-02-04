from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class IndexPage(QWidget):
    def __init__(self):
        super().__init__()

        chapters_list = ["TUTORIAL", "LEVELS", "HELP", "PROFILE"]

        vlayout = QVBoxLayout(self)
        vlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        path = "/home/mario/Project/XSSify/XSSify/icons/right_arrow.png"

        # Adding icon and indices to layout
        for chapter in chapters_list:
            arrow_icon = ArrowIcon(path, icon_size=(50,50))
            
            hlayout = QHBoxLayout()
            hlayout.addWidget(arrow_icon)
            label = QLabel(chapter)
            label.setStyleSheet("font-size: 40px; letter-spacing: 10px; font-weight: bold;")
            hlayout.addWidget(label)
            hlayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            
            vlayout.addLayout(hlayout)


# Function to create arrow icon
class ArrowIcon(QWidget):
    def __init__(self, png_path, icon_size):
        super().__init__()

        pixmap = QPixmap(png_path).scaled(*icon_size)

        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)