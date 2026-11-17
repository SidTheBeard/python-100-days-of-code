class QuizBrain:
    def __init__(self, list):
        print("Brain booting up...")
        self.question_number = 0
        self.score = 0
        self.question_list = list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        print(f"\n\nYour score is: {self.score}")
        entry = input(f"Q #{self.question_number}: {self.question_list[self.question_number].text} (True/False): \n\n")
        entry = entry.lower()
        self.process_input(entry)
        self.question_number += 1

    def process_input(self, entry):
        if entry != "skip":
            if entry == self.question_list[self.question_number].answer.lower():
                print("Correct!\n\n")
                self.score += 1
            else:
                print(f"Incorrect, the correct answer was {self.question_list[self.question_number].answer}.\n\n")
