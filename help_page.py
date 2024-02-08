from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt

class HelpPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Create a horizontal layout for the hamburger menu and label
        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(top_layout)

        hamburger_icon = QLabel("☰")
        hamburger_icon.setStyleSheet("font-size: 30px; color: #2DD096; margin-left: 50px;")

        top_layout.addWidget(hamburger_icon)
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

        # Iterate over specific words and make them bold
        for word in ["Tutorials", "Levels", "Tutorials", "Levels"]:
            text = text.replace(word, f"<em>{word}</em>")

        paragraph_label.setText(text)

        parent_layout.addWidget(paragraph_label, alignment=Qt.AlignmentFlag.AlignTop)