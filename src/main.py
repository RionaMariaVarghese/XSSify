import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont, QColor, QIcon
from welcome_page import WelcomePage
from index_page import IndexPage
from tutorial_page import TutorialPage
from levels_page import LevelsPage
from help_page import HelpPage
from profile_page import ProfilePage

class MainWindow(QMainWindow):
    navigateToPage = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        welcome_page = WelcomePage()
        self.setCentralWidget(welcome_page)

        # App window title and icon
        self.setWindowTitle("XSSify")
        icon_path = "/home/mario/Project/XSSify/XSSify/icons/bug.png"
        self.setWindowIcon(QIcon(icon_path))

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
        self.timer.start(5000)

        # Create instances of pages
        self.index_page = IndexPage()
        self.tutorial_page = TutorialPage()
        self.levels_page = LevelsPage()
        self.help_page = HelpPage()
        self.profile_page = ProfilePage()

        # Add pages to stacked widget
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.index_page)
        self.stackedWidget.addWidget(self.tutorial_page)
        self.stackedWidget.addWidget(self.levels_page)
        self.stackedWidget.addWidget(self.help_page)
        self.stackedWidget.addWidget(self.profile_page)
        self.setCentralWidget(self.stackedWidget)

        # Connect signals
        self.index_page.navigateToPage.connect(self.navigate_to_page)
        self.tutorial_page.returnToIndexSignal.connect(self.show_index_page)
        self.levels_page.returnToIndexSignal.connect(self.show_index_page)
        self.help_page.returnToIndexSignal.connect(self.show_index_page)
        self.profile_page.returnToIndexSignal.connect(self.show_index_page)

    def show_index_page(self):
        self.timer.stop()
        self.stackedWidget.setCurrentWidget(self.index_page)

    def navigate_to_page(self, page_name):
        if page_name == "TUTORIAL":
            self.stackedWidget.setCurrentWidget(self.tutorial_page)
        elif page_name == "LEVELS":
            self.stackedWidget.setCurrentWidget(self.levels_page)
        elif page_name == "HELP":
            self.stackedWidget.setCurrentWidget(self.help_page)
        elif page_name == "PROFILE":
            self.stackedWidget.setCurrentWidget(self.profile_page)

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
