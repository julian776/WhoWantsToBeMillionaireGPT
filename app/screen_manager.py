from time import sleep
from os import system, name

class screen_manager:
    def show_question(question):
        print(question[0], "\n")
        print("a)  ", question[1], "b)  ", question[2])
        print("c)  ", question[3], "d)  ", question[4], "\n")

    def screen_updater(manager, question):
        round = manager.get_round()
        cash = manager.get_cash()
        screen_manager.clean()
        print("\nRound ",round,"      Cash Earned", cash, "\n")
        screen_manager.show_question(question)

    def clean():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    

        
    
    