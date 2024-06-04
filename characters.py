class Character:
    def __init__(self, name):
        self.name = name
        self.approval = 0

    def change_approval(self, amount):
        self.approval += amount
        print(f"{self.name}'s approval is now {self.approval}.")

    def is_willing_to_sacrifice(self):
        return self.approval >= 10

    def might_sacrifice_player(self):
        return self.approval <= -10

class Stranger(Character):
    def __init__(self, name):
        super().__init__(name)
        self.is_killer = False

    def decide_to_kill(self):
        self.is_killer = True

    def ask_questions(self):
        print("\nThe Stranger asks you a series of questions:")
        questions = [
            ("Do you think it's okay to hurt others to survive?", ["yes", "no"]),
            ("Would you leave someone behind to save yourself?", ["yes", "no"]),
            ("Do you think the weak deserve to die?", ["yes", "no"])
        ]
        for question, answers in questions:
            print(question)
            choice = input(f"Type '{answers[0]}' or '{answers[1]}': ").lower()
            if choice == answers[0]:
                self.change_approval(10)
            else:
                self.change_approval(-10)
