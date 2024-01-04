# Create a quiz application with the following specifications:
# Create 3 quizzes named Quiz 1, Quiz 2, and Quiz 3.
# Each quiz should have 5-10 questions.
# Student A should be able to attempt Quiz 1, Student B Quiz 2, and Student C Quiz 3.
# Implement a Leaderboard that displays the ranks of all students together.



class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def display_questions(self):
        for i, question in enumerate(self.questions, 1):
            print(f"{i}. {question}")

    def take_quiz(self):
        answers = []
        print(f"\n--- {self.name} ---")
        for i, question in enumerate(self.questions, 1):
            answer = input(f"Q{i}. {question}: ").lower()
            answers.append(answer)
        return answers


class Leaderboard:
    def __init__(self):
        self.students = {}

    def update_leaderboard(self, student_name, quiz, score):
        if student_name not in self.students:
            self.students[student_name] = {}
        self.students[student_name][quiz] = score

    def display_leaderboard(self):
        sorted_students = sorted(self.students.items(), key=lambda x: sum(x[1].values()), reverse=True)
        print("\n--- Leaderboard ---")
        for rank, (student, scores) in enumerate(sorted_students, 1):
            total_score = sum(scores.values())
            print(f"{rank}. {student} - Total Score: {total_score}")



quiz1 = Quiz("Quiz 1", ["What is 2 + 2?", "What is the capital of France?", "Python is a programming language. (True/False)"])
quiz2 = Quiz("Quiz 2", ["Who is the president of the United States?", "What is the square root of 25?"])
quiz3 = Quiz("Quiz 3", ["What is the largest mammal on Earth?", "What is the currency of Japan?"])


leaderboard = Leaderboard()


student_a_answers = quiz1.take_quiz()
student_b_answers = quiz2.take_quiz()
student_c_answers = quiz3.take_quiz()


leaderboard.update_leaderboard("Student A", "Quiz 1", student_a_answers.count("4"))
leaderboard.update_leaderboard("Student B", "Quiz 2", student_b_answers.count("joe biden") + student_b_answers.count("5"))
leaderboard.update_leaderboard("Student C", "Quiz 3", student_c_answers.count("blue whale") + student_c_answers.count("yen"))

leaderboard.display_leaderboard()
