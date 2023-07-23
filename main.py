
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QButtonGroup, QRadioButton, QMessageBox

# Sample quiz data (You can replace this with your own questions and answers)
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "answer": 1
    },
    {
        "question": "What is 8 + 5?",
        "options": ["10", "12", "13", "15"],
        "answer": 3
    }
]

class QuizGameApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Game")
        self.quiz_data = random.sample(quiz_data, len(quiz_data))
        self.total_questions = len(self.quiz_data)
        self.score = 0
        self.current_question = 0

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.question_label = QLabel(self.quiz_data[self.current_question]["question"])
        main_layout.addWidget(self.question_label)

        self.options_group = QButtonGroup()
        options_layout = QVBoxLayout()

        for idx, option in enumerate(self.quiz_data[self.current_question]["options"]):
            radio_button = QRadioButton(option)
            self.options_group.addButton(radio_button, idx)
            options_layout.addWidget(radio_button)

        main_layout.addLayout(options_layout)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_answer)
        main_layout.addWidget(self.submit_button)

    def check_answer(self):
        selected_button = self.options_group.checkedId()
        if selected_button == self.quiz_data[self.current_question]["answer"] - 1:
            self.score += 1

        self.current_question += 1

        if self.current_question < self.total_questions:
            self.update_question()
        else:
            self.show_result()

    def update_question(self):
        self.question_label.setText(self.quiz_data[self.current_question]["question"])

        for idx, option in enumerate(self.quiz_data[self.current_question]["options"]):
            self.options_group.button(idx).setText(option)

    def show_result(self):
        result_text = f"Quiz completed!\nYour score: {self.score}/{self.total_questions}"
        QMessageBox.information(self, "Quiz Completed", result_text, QMessageBox.Ok)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_app = QuizGameApp()
    game_app.show()
    sys.exit(app.exec_())
