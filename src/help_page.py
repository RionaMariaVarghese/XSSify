import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt

class HelpPage(QWidget):
    returnToIndexSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Create a horizontal layout for the hamburger menu and label
        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(top_layout)

        # self.hamburger_icon = QPushButton('\u2630', self)
        # self.hamburger_icon.setStyleSheet("border: none; font-size: 30px; color: #2DD096; margin-left: 50px;")
        # self.hamburger_icon.clicked.connect(self.show_menu)

        self.index_button = QPushButton("☰")
        self.index_button.setStyleSheet("font-size: 15px; color: #2DD096;")
        self.index_button.clicked.connect(self.emit_return_to_index_signal)
        layout.addWidget(self.index_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # top_layout.addWidget(self.hamburger_icon)
        top_layout.addWidget(self.index_button)
        top_layout.addSpacing(30)

        help_label = QLabel("HELP")
        help_label.setStyleSheet("font-size: 40px; letter-spacing: 10px; font-weight: bold;")
        top_layout.addWidget(help_label)

        # Scroll Area
        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("border: none; background-color: #252839;")
        layout.addWidget(scroll_area)

        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)
        inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(inner_widget)
        scroll_area.setWidgetResizable(True)

        self.add_paragraph("A walkthrough on how to use this application.", inner_layout)

        self.add_heading("TUTORIALS:", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            This section is where you will be learning the concepts of XSS and how to implement them. You will be awarded coins on completing each tutorial and can then use it to access Hints in the <span>Levels</span> Section. Your progress will also be tracked.
        """, inner_layout)

        self.add_heading("LEVELS:", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            This section is designed to test the knowledge you have gained from the <span>Tutorials</span>. You will be given coins and badges on completing each level. One can access this section only after completing the <span>Tutorials</span> Section. You can utilize the hints using the coins you have previously earned.
        """, inner_layout)

        self.add_heading("PROFILE:", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            This section is used to track your progress, badges, and coins earned.
        """, inner_layout)

    def add_heading(self, text, parent_layout, font_size, alignment):
        heading_label = QLabel(text)
        heading_label.setStyleSheet(f"font-size: {font_size}px; text-decoration: underline; letter-spacing: 2px;")
        parent_layout.addWidget(heading_label, alignment=alignment)

    def add_paragraph(self, text, parent_layout):
        paragraph_label = QLabel(text)
        paragraph_label.setStyleSheet("font-size: 25px; text-align: justify; padding: 10px 60px 60px 60px; letter-spacing: 2px;")
        paragraph_label.setWordWrap(True)

        paragraph_label.setTextFormat(Qt.TextFormat.RichText)
        paragraph_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        for word in ["Tutorials", "Levels", "Tutorials", "Levels"]:
            text = text.replace(word, f"<em>{word}</em>")

        paragraph_label.setText(text)

        parent_layout.addWidget(paragraph_label, alignment=Qt.AlignmentFlag.AlignTop)

    # def show_menu(self):
    #     self.navigateToIndex.emit()

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()