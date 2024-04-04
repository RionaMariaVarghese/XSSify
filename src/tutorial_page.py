import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt
from tutorial_db import Session, TutorialPageContent

class TutorialPage(QWidget):
    returnToIndexSignal = pyqtSignal()

    def __init__(self, session):
        super().__init__()

        self.page_state = "initial"
        self.session = session
        self.chapters = self.fetch_chapter_titles()
        self.current_chapter_index = 0

        main_layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        self.setup_index_button(top_layout)
        main_layout.addLayout(top_layout)

        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("border: none; background-color: #252839;")
        scroll_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(scroll_area)

        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)
        inner_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_area.setWidget(inner_widget)
        scroll_area.setWidgetResizable(True)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        inner_layout.addWidget(self.content_widget)

        self.bottom_layout = QHBoxLayout()
        main_layout.addLayout(self.bottom_layout)

        self.setLayout(main_layout)

        self.show_initial_page()

    def setup_index_button(self, layout):
        index_button = QPushButton("☰")
        index_button.clicked.connect(self.emit_return_to_index_signal)
        index_button.setStyleSheet(
            """
                QPushButton {
                    font-size: 25px;
                    background-color: rgba(0, 0, 0, 0);
                    color: #2DD096;
                    padding: 2px 25px;
                    border-radius: 5px;
                }
                
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }
                
                QPushButton:pressed {
                    background-color: rgba(255, 255, 255, 0.2);
                }
            """
        )
        layout.addWidget(index_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def show_initial_page(self):
        self.clear_layout(self.content_layout)
        self.clear_layout(self.bottom_layout)

        label = QLabel("This is the Tutorials Page")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(label)

        btn_cont = QPushButton("Continue")
        btn_cont.clicked.connect(self.show_current_chapter)
        self.bottom_layout.addWidget(btn_cont)

    def show_page_by_title(self, title):
        self.clear_layout(self.content_layout)
        self.clear_layout(self.bottom_layout)

        tutorial_content = self.fetch_tutorial_content(title)
        if tutorial_content:
            heading = QLabel(tutorial_content.title)
            heading.setStyleSheet("font-size: 36px; color: #2DD096; font-weight: bold; text-decoration: underline;")
            heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

            content = QLabel(tutorial_content.content)
            content.setStyleSheet("font-size: 24px; color: white; font-weight: regular; text-align: justify;")
            content.setAlignment(Qt.AlignmentFlag.AlignLeft)
            content.setWordWrap(True)

            self.content_layout.addWidget(heading)
            self.content_layout.addWidget(content)

            self.add_navigation_buttons()

    def fetch_tutorial_content(self, title):
        tutorial_content = self.session.query(TutorialPageContent).filter_by(title=title).first()
        return tutorial_content

    def fetch_chapter_titles(self):
        titles = [chapter.title for chapter in self.session.query(TutorialPageContent).all()]
        return titles

    def show_current_chapter(self):
        title = self.chapters[self.current_chapter_index]
        self.show_page_by_title(title)

    def show_previous_chapter(self):
        self.current_chapter_index -= 1
        if self.current_chapter_index < 0:
            self.current_chapter_index = len(self.chapters) - 1
        self.show_current_chapter()

    def show_next_chapter(self):
        self.current_chapter_index += 1
        if self.current_chapter_index >= len(self.chapters):
            self.current_chapter_index = 0
        self.show_current_chapter()

    def add_navigation_buttons(self):
        self.clear_layout(self.bottom_layout)

        btn_prev = QPushButton("Previous")
        btn_prev.clicked.connect(self.show_previous_chapter)
        self.bottom_layout.addWidget(btn_prev)

        btn_next = QPushButton("Next")
        btn_next.clicked.connect(self.show_next_chapter)
        self.bottom_layout.addWidget(btn_next)

        if self.current_chapter_index == 0:
            btn_prev.setEnabled(False)

        if self.current_chapter_index == len(self.chapters) - 1:
            btn_next.setEnabled(False)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Tutorial Page")

#         session = Session()

#         tutorial_page = TutorialPage(session)
#         tutorial_page.returnToIndexSignal.connect(self.return_to_index_page)

#         self.setCentralWidget(tutorial_page)
#         self.showMaximized()

#     def return_to_index_page(self):
#         print("Returning to index page")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
