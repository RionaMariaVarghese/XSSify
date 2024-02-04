from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

class IndexPage(QWidget):
    navigateToPage = pyqtSignal(str)

    def __init__(self):
        super().__init__()



        chapters_list = ["TUTORIAL", "LEVELS", "HELP", "PROFILE"]
        path = "/home/mario/Project/XSSify/XSSify/icons/right_arrow.png"

        vlayout = QVBoxLayout(self)
        vlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        for chapter in chapters_list:
            arrow_icon = ArrowIcon(path, icon_size=(50, 50))
            label = ClickableLabel(chapter, self.navigateToPage.emit)
            label.setStyleSheet("font-size: 40px; letter-spacing: 10px; font-weight: bold;")

            hlayout = QHBoxLayout()
            hlayout.addWidget(arrow_icon)
            hlayout.addWidget(label)
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

class ClickableLabel(QLabel):
    def __init__(self, label_name='', callback=None, parent=None):
        super().__init__(label_name, parent)
        self.callback = callback

    def enterEvent(self, event):
        # Set underlined style when mouse enters
        self.setStyleSheet("text-decoration: underline; font-size: 40px; letter-spacing: 10px; font-weight: bold;")
        QApplication.setOverrideCursor(Qt.CursorShape.PointingHandCursor)

    def leaveEvent(self, event):
        # Reset style when mouse leaves
        self.setStyleSheet("text-decoration: none; font-size: 40px; letter-spacing: 10px; font-weight: bold;")

    def mousePressEvent(self, event):
        if self.callback:
            self.callback(self.text())