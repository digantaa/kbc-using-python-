class KBC:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
        self.ask_question()

    def ask_question(self):
        print(self.question)
        for key, value in self.options.items():
            print(f"{key}: {value}")

    def check_answer(self):
        user_answer = input("Answer: ").lower()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer in self.options and self.options[user_answer].lower() == self.answer.lower():
                print("Correct Answer")
                print("You have won a reward")
                return True
            else:
                print("Wrong Answer")
                return False
        elif user_answer == self.answer.lower():
            print("Correct Answer")
            print("You have won the game")
            return True
        else:
            print("Wrong Answer")
            return False

    def next_question(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
        self.ask_question()
        self.check_answer()

quiz = KBC("What is the capital of India?", {1: "Delhi", 2: "Mumbai", 3: "Kolkata", 4: "Chennai"}, "Delhi")
if quiz.check_answer():
    quiz.next_question("What is the name of my favourite movie?", {1: "Cars", 2: "Interstellar", 3: "Singham", 4: "Baghi"}, "Interstellar")
