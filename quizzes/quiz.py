import datetime
import sys

class Quiz:
    def __init__(self):
        self.name=""
        self.description=""
        self.questions =[]
        self.score=0
        self.correct_count=0
        self.total_points=0

    def print_header(self):
        print("\n\n----------------------------------------------")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("\n\n----------------------------------------------")

    def print_results(self, quiztaker,thefile= sys.stdout):
        print("\n\n----------------------------------------------",file=thefile,flush=True)
        print(f"RESULTS FOR {quiztaker}",file=thefile,flush=True)
        print(f"Date : {datetime.datetime.today()}",file=thefile,flush=True)
        print(f"QUESTION: {self.correct_count} out of {len(self.questions)} correct",file=thefile,flush=True)
        print(f"SCORE: {self.score} points out of possible {self.total_points}",file=thefile,flush=True)
        print("\n\n----------------------------------------------",file=thefile,flush=True)

    def take_quiz(self):
        self.score=0
        self.correct_count=0
        for q in self.questions:
            q.is_correct=False
        self.print_header()
        for q in self.questions:
            q.ask()
            if(q.is_correct):
                self.correct_count += 1
                self.score += q.points

        print("\n\n----------------------------------------------")
        return (self.score,self.correct_count,self.total_points)
    
class Question:
    def __init__(self):
        self.points=0
        self.correct_answer=""
        self.text=""
        self.is_correct= False 


class QuestionTF(Question):
    def __init__(self):
        super().__init__()
    
    def ask(self):
        while(True):
            print(f"(T)rue of (F)alse: {self.text}")
            response = input("? ")

            if len(response) == 0:
                print("That not the valid respose. Please try again")
                continue
            response = response.lower()
            if response[0] != "t" and response[0] != "f":
                print("That not the valid respose. Please try again")
                continue
            if response[0] == self.correct_answer:
                self.is_correct = True

            break

class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while(True):
            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response= input("? ")

            if len(response) == 0:
                print("That not the valid respose. Please try again")
                continue
            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True

            break

class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""

if __name__=="__main__":
    qz = Quiz()
    qz.name = "Sample Quiz"
    qz.description = "This is a sample quiz!"

    q1= QuestionMC()
    q1.text="=> What is the output of the following Python code?"
    q1.points=5
    q1.correct_answer="b"
    ans=Answer()
    ans.name="a"
    ans.text="Hello2"
    q1.answers.append(ans)
    ans=Answer()
    ans.name="b"
    ans.text="TypeError: can only concatenate str (not int) to str"
    q1.answers.append(ans)
    ans=Answer()
    ans.name="c"
    ans.text="2"
    q1.answers.append(ans)
    ans=Answer()
    ans.name="d"
    ans.text="Hello"
    q1.answers.append(ans)
    qz.questions.append(q1)

    q2 = QuestionTF()
    q2.text= "=> Python is a dynamically typed language?"
    q2.points=2
    q2.correct_answer="t"
    qz.questions.append(q2)

    q3= QuestionMC()
    q3.text="=> What does the len() function do in Python?"
    q3.points=5
    q3.correct_answer="c"
    ans=Answer()
    ans.name="a"
    ans.text="Converts a value to a string"
    q3.answers.append(ans)
    ans=Answer()
    ans.name="b"
    ans.text="Returns the square root of a number"
    q3.answers.append(ans)
    ans=Answer()
    ans.name="c"
    ans.text="Returns the length of a list or string"
    q3.answers.append(ans)
    ans=Answer()
    ans.name="d"
    ans.text="None of the above"
    q3.answers.append(ans)
    qz.questions.append(q3)

    q4 = QuestionTF()
    q4.text= "=> A Python set can contain duplicate elements?"
    q4.points=3
    q4.correct_answer="f"
    qz.questions.append(q4)


    qz.total_points=q1.points+q2.points+q3.points+q4.points
    result = qz.take_quiz()
    print(result)