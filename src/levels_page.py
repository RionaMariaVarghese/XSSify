import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QRadioButton
from firebase_level import get_data_from_firestore

class Levels(QMainWindow):
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

        self.label_question = QLabel()
        self.layout.addWidget(self.label_question)

        # Add radio buttons for multiple-choice questions
        self.radio_buttons = []
        for i in range(4):
            radio_button = QRadioButton()
            self.radio_buttons.append(radio_button)
            self.layout.addWidget(radio_button)

        # Add line edit for written answers
        self.answer_field = QLineEdit()
        self.layout.addWidget(self.answer_field)

        self.btn_submit = QPushButton("Submit")
        self.btn_submit.clicked.connect(self.next_question)
        self.layout.addWidget(self.btn_submit)

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

        # print("Selected Option Text:", selected_option_text)  # Debugging statement

        correct_answer = self.questions[self.question_index]["answer"].strip().lower()

        # print("Correct Answer:", correct_answer)  # Debugging statement

        if selected_option_text is not None:
            if selected_option_text == correct_answer:
                self.score += 1
                QMessageBox.information(self, "Correct answer")

        if typed_answer.lower() == correct_answer:
            self.score += 1
            QMessageBox.information(self, "Correct answer")

        else:
            QMessageBox.information(self, "Incorrect answer")


        # print("User Input:", typed_answer)  # Debugging Statement

        self.question_index += 1
        self.show_question()


    def show_result(self):
        result_msg = f"Your score: {self.score}/{len(self.questions)}"
        QMessageBox.information(self, "Quiz Finished", result_msg)
        self.close()

def main():
    app = QApplication(sys.argv)
    quiz_app = Levels()
    quiz_app.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
