class Survey:
    def __init__(self, question):
        self.question = question
        self.answers = []

    def show_question(self):
        print(self.question)

    def add_answer(self, answer):
        self.answers.append(answer)

    def show_results(self):
        for answer in self.answers:
            print(answer)

# question = Survey("What is your name?")
# name_survey = Survey(question)
# question.show_question()
# while True:
#     answer = input("name:")
#     if answer == "quit":
#         break
#     name_survey.add_answer(answer)
#
# name_survey.show_results()