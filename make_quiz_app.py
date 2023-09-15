class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.answer = answer
        self.choices = choices

    def check_answer(self,answer):
        return self.answer== answer

q1 = Question("What is 3+5?", ["9", "7", "5", "8", "3"], "8")
q2 = Question("What is 9-5?", ["14", "11", "3", "4", "7"], "4")
q3 = Question("What is the capital city of Turkey?", ["İstanbul", "Ankara", "İzmir", "Hatay", "Kocaeli"], "Ankara")

questions=[q1,q2,q3]

class Quiz():
    def __init__(self,questions):
        self.questions=questions
        self.index = 0
        self.score=0

    def make_quiz(self):
        self.display_question()
        
    def get_question(self):
        question=self.questions[self.index]
        return question
    
    def display_question(self):
        question=self.get_question()

        print(f"Question- {self.index+1}: {question.text}")
        for c in question.choices:
            print(c)

        answer=input("answer: ")

        self.check(answer)

    def check(self,answer):
        question=self.get_question()

        if question.answer==answer:
            self.score+=1
        self.index+=1

        if self.index!=len(self.questions):
            self.display_question()
        else:
            self.show_score()
        
    def show_score(self):
        print(f"Quiz is finished. Your score is: {self.score}")

q1=Quiz(questions)

q1.make_quiz()