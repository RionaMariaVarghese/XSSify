import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor
from welcome_page import WelcomePage
from index_page import IndexPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        welcome_page = WelcomePage()
        self.setCentralWidget(welcome_page)

        # App window title and icon
        self.setWindowTitle("XSSify")

        # Setting default font
        app_font = QFont("JetBrains Mono")
        QApplication.instance().setFont(app_font)

        # Setting main bg color
        main_window_color = QColor("#252839")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), main_window_color)
        self.setPalette(p)

        # Timer for welcome page
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_index_page)
        self.timer.start(2500)

    def show_index_page(self):
        self.timer.stop()
        index_page = IndexPage()
        self.setCentralWidget(index_page)

    # Centering contents
    def center_window(self):
        screen_geo = QApplication.primaryScreen().geometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.move(x, y)

# Main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setMinimumSize(1000, 800)
    widget.show()
    widget.center_window()
    sys.exit(app.exec())
