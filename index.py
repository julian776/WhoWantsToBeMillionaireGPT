from app import game
from app.saver import saver
from app.loaders import loaders
from app.screen_manager import screen_manager #Easy notation

QUESTIONS = ["questions1.txt", "questions2.txt", "questions3.txt", "questions4.txt", "questions5.txt"]
SAVE_FILE = "save/save.txt"

if __name__ == '__main__':
    loaders.load_game()
    while True: #Wait yor a valid input
        request = loaders.load_menu()
        if request == "0":
            validate = "registered"
            while validate == "registered": #Validate if already registered
                user = input("Register your username: ")
                validate = saver.validate_user(user)
            actual_game = game.game(1, 00)
            break
        elif request == "1":
            user = input("Please type your username: ")
            actual_game = loaders.load_user(SAVE_FILE ,user)
            break
        else:
            print("\nPlease enter again.")
    while actual_game.get_round() < 6: #Loop of questions and answers
        question = loaders.load_question(QUESTIONS, actual_game.get_round())
        screen_manager.screen_updater(actual_game, question)
        print("To save your progress type save")
        answer = input("Type your answer: ")
        game.game_manager.validate_answer(actual_game, answer, question, user)
    print("\nYou Won ", actual_game.get_cash())
    saver(actual_game, user, file="legend.txt")    



    
    


