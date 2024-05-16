from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

class IndexPage(QWidget):
    navigateToPage = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setup_layout()
    
    def setup_layout(self):
        chapters_list = ["TUTORIAL", "LEVELS", "HELP", "ABOUT"]
        path = "src/icons/right_arrow.png"

        vlayout = QVBoxLayout(self)
        vlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        for chapter in chapters_list:
            arrow_icon = ArrowIcon(path, icon_size=(50, 50))
            button = QPushButton(chapter)
            button.clicked.connect(lambda _, ch=chapter: self.navigateToPage.emit(ch))
            button.setStyleSheet("""
                QPushButton {
                    font-size: 30px;
                    letter-spacing: 10px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0);
                    border: 1px solid #FFFFFF;
                    color: #2DD096;
                    padding: 20px 40px;
                    border-radius: 10px;
                    margin: 6px;
                }
                
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }
                
                QPushButton:pressed {
                    background-color: rgba(255, 255, 255, 0.2);
                }
                """
            )

            hlayout = QHBoxLayout()
            hlayout.addWidget(arrow_icon)
            hlayout.addWidget(button)
            hlayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

            vlayout.addLayout(hlayout)

class ArrowIcon(QWidget):
    def __init__(self, png_path, icon_size):
        super().__init__()
        pixmap = QPixmap(png_path).scaled(*icon_size)
        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
