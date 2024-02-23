
from quizmanager import QuizManager

class QuizApp:
    QUIZ_FOLDER="Quizzes"
    def __init__(self):
        self.username= ""
        self.qm=QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        # print the greeting at startup
        self.greeting()

        self.username= input("What is your name? ")
        print(f"Welcome, {self.username}!")
        print()

    
    def greeting(self):
        print("------------------------------")
        print("----Welcome to Python Quiz----")
        print("------------------------------")
        print()
    
    def menu_header(self):
        print("------------------------------")
        print("Please make a selection:")
        print("(M): Repeat the menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")
    
    def menu_error(self):
        print("That is not a valid selection. Please try again")

    def goodbye(self):
        print("----------------------------------------------")
        print(f"Thanks for using Python Quiz, {self.username}!")
        print("----------------------------------------------")
    
    def menu(self):
        self.menu_header()

        selection=""
        while(True):
            selection=input("selection?")

            if len(selection) == 0:
                self.menu_error()
                continue
            selection=selection.capitalize()
            if selection[0] == 'E':
                self.goodbye()
                break
            elif selection[0] == 'M':
                self.menu_header()
                continue
            elif selection[0] == 'L':
                print("\nAvailable Quizzes Are:")
                self.qm.list_quizzes()
                print("------------------------\n")
                continue
            elif selection[0] == 'T':
                try:
                    quiznum= int(input("Quiz number"))
                    print(f"You have selected quiz {quiznum}")
                    self.qm.take_quiz(quiznum,self.username)
                    self.qm.print_results()
                    dosave=input("Save the results? (y/n):")
                    dosave = dosave.capitalize()
                    if len(dosave)>0 and dosave[0]=='Y':
                        self.qm.save_results()
                except:
                    self.menu_error()
            else:
                self.menu_error()

    def run(self):
        self.startup()
        self.menu()

if __name__=="__main__":
    app=QuizApp()
    app.run()
    
