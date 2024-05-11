import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QRadioButton
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont
from level_db import Session, LevelPageContent

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
        self.setup_intro_ui()

    def setup_intro_ui(self):
        font = QFont("JetBrains Mono", 15)
        layout = QVBoxLayout()

        label_intro = QLabel("Welcome to the Levels!\n\nRules and Conditions:")
        label_intro.setFont(font)
        label_intro.setStyleSheet("letter-spacing: 2px; font-weight: bold; color: #2DD096;")
        label_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_intro)

        label_rules = QLabel("- It is reccommended to go through the Tutorial Sections before attending this section.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        label_rules = QLabel("- This quiz can be taken any number of times.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        label_rules = QLabel("- Each question will have multiple-choice options or require user input.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        label_rules = QLabel("- For multiple-choice questions, select the correct option.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        label_rules = QLabel("- For questions requiring user input, type your answer in the provided field.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        label_rules = QLabel("- Please ensure that the answer typed or marked is the one that you had in mind before submitting the same.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        label_rules = QLabel("- Pratice till you get the perfect score.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        label_rules = QLabel("- Click the 'Start Levels' button to begin.")
        label_rules.setFont(font)
        layout.addWidget(label_rules)

        btn_start = QPushButton("Start Levels")
        btn_start.setFont(font)
        btn_start.setStyleSheet("""
                QPushButton {
                    font-size: 15px;
                    letter-spacing: 5px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0);
                    border: 1px solid #FFFFFF;
                    color: #2DD096;
                    padding: 10px 20px;
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
        btn_start.clicked.connect(self.show_question)
        layout.addWidget(btn_start, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_questions(self):
        session = Session()
        self.questions = session.query(LevelPageContent).all()
        session.close()
        # self.questions = get_data_from_firestore()

    def setup_ui(self):
        font = QFont("JetBrains Mono", 15)
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

        options_layout = QVBoxLayout()
        options_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        options_wrapper_layout = QHBoxLayout()
        options_wrapper_layout.addStretch()
        options_wrapper_layout.addLayout(options_layout)
        options_wrapper_layout.addStretch()
        self.layout.addLayout(options_wrapper_layout)
        
        options_layout.addStretch()

        self.label_question = QLabel()
        self.label_question.setFont(font)
        options_layout.addWidget(self.label_question, alignment=Qt.AlignmentFlag.AlignCenter)

        self.radio_buttons = []
        for i in range(4):
            radio_button = QRadioButton()
            radio_button.setChecked(False)
            self.radio_buttons.append(radio_button)
            radio_button.setFont(font)
            options_layout.addWidget(radio_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.answer_field = QLineEdit()
        self.answer_field.setFont(font)
        options_layout.addWidget(self.answer_field)

        options_layout.addStretch()

        self.btn_submit = QPushButton("Submit")
        self.btn_submit.setFont(font)
        self.btn_submit.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
                    letter-spacing: 10px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0);
                    border: 1px solid #FFFFFF;
                    color: #2DD096;
                    padding: 10px 20px;
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
        self.btn_submit.clicked.connect(self.next_question)
        self.layout.addWidget(self.btn_submit)

        # Button to return to Index after questions finish
        self.btn_return = QPushButton("Return to Index Page")
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
                    letter-spacing: 10px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0);
                    border: 1px solid #FFFFFF;
                    color: #2DD096;
                    padding: 10px 20px;
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
        self.btn_return.clicked.connect(self.emit_return_to_index_signal)
        self.btn_return.hide()
        self.layout.addWidget(self.btn_return)


    def reset(self):
        self.question_index = 0
        self.score = 0
        self.btn_submit.show()
        self.btn_return.hide()
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
        self.answer_field.clear()
        self.load_questions()
        self.setup_ui()
        self.show_question()

    def show_question(self):
        self.centralWidget().deleteLater()
        self.setup_ui()
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            question = question_data.question
            options = [question_data.option1, question_data.option2, question_data.option3, question_data.option4]
            requires_input = question_data.requires_input

            self.label_question.setText(question)
            self.answer_field.clear()

            if requires_input:
                self.answer_field.show()
                for radio_button in self.radio_buttons:
                    radio_button.hide()
            else:
                if options:
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
            for radio_button in self.radio_buttons:
                radio_button.hide()
            self.answer_field.hide()
            self.show_result()


    def next_question(self):
        typed_answer = self.answer_field.text().strip()

        selected_option_text = None
        for i, radio_button in enumerate(self.radio_buttons):
            if radio_button.isChecked():
                selected_option_text = self.radio_buttons[i].text().strip().lower()
                break

        correct_answer = self.questions[self.question_index].answer.strip().lower()

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
        self.reset()
        self.returnToIndexSignal.emit("")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)
        self.levels_page = LevelsPage()
        self.setCentralWidget(self.levels_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
