from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QRadioButton
from firebase_level import get_data_from_firestore
from PyQt6.QtCore import pyqtSignal

class LevelsPage(QMainWindow):
    returnToIndexSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Levels")
        self.setGeometry(100, 100, 600, 400)

        # Setting necessary variables
        self.question_index = 0
        self.score = 0
        self.questions = []

        self.load_questions()

        self.setup_ui()
        self.show_question()

    def load_questions(self):
        self.questions = get_data_from_firestore()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        top_layout = QHBoxLayout()
        self.layout.addLayout(top_layout)

        self.hamburger_menu_button = QPushButton("☰")
        self.hamburger_menu_button.setStyleSheet("""
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
        """)
        self.hamburger_menu_button.clicked.connect(self.emit_return_to_index_signal)
        top_layout.addWidget(self.hamburger_menu_button)

        # Add a spacer to push the hamburger menu button to the left
        top_layout.addStretch()

        self.label_question = QLabel()
        self.layout.addWidget(self.label_question)

        self.radio_buttons = []
        for i in range(4):
            radio_button = QRadioButton()
            self.radio_buttons.append(radio_button)
            self.layout.addWidget(radio_button)

        self.answer_field = QLineEdit()
        self.layout.addWidget(self.answer_field)

        self.btn_submit = QPushButton("Submit")
        self.btn_submit.clicked.connect(self.next_question)
        self.layout.addWidget(self.btn_submit)

        # Button to return to Index after questions finish
        self.btn_return = QPushButton("Return to Index Page")
        self.btn_return.clicked.connect(self.emit_return_to_index_signal)
        self.btn_return.hide()
        self.layout.addWidget(self.btn_return)

    def show_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.label_question.setText(question_data["question"])
            self.answer_field.clear()

            if "options" in question_data:
                options = question_data["options"]
                for i, option in enumerate(options):
                    self.radio_buttons[i].setText(option)
                self.answer_field.hide()
                for radio_button in self.radio_buttons:
                    radio_button.show()
            else:
                self.answer_field.show()
                for radio_button in self.radio_buttons:
                    radio_button.hide()
        else:
            self.show_result()

    def next_question(self):
        typed_answer = self.answer_field.text().strip()

        selected_option_text = None
        for i, radio_button in enumerate(self.radio_buttons):
            if radio_button.isChecked():
                selected_option_text = self.radio_buttons[i].text().strip().lower()
                break

        correct_answer = self.questions[self.question_index]["answer"].strip().lower()

        if selected_option_text is not None:
            if selected_option_text == correct_answer:
                self.score += 1
                QMessageBox.information(self, "MCQAnswer", "Correct answer")

        if typed_answer.lower() == correct_answer:
            self.score += 1
            QMessageBox.information(self, "TAnswer", "Correct answer")

        if selected_option_text != correct_answer and typed_answer.lower() != correct_answer:
            QMessageBox.information(self, "Answer", "Incorrect answer")

        self.question_index += 1
        self.show_question()

    def show_result(self):
        result_msg = f"Your score: {self.score}/{len(self.questions)}"
        QMessageBox.information(self, "Quiz Finished", result_msg)
        self.btn_return.show()
        self.btn_submit.hide()
    
    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit("")
