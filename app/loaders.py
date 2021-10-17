from app.screen_manager import screen_manager
import numpy as np
from time import sleep
from app.game import game 

class loaders:
    def load_game():
        screen_manager.clean()
        text = open("instructions.txt", "r")
        for line in text:
            print(line)
        text.close()
        input("Press enter to continue")
        screen_manager.clean()
        
    def load_menu():
        print("To start a new game type 0")
        print("Load a game type 1")
        request = input("Type what you like to do: ")
        return request

    def load_question(requirements, round):
        """load_question get one question from the file
        of a specific round"""
        questions = []
        file_path = requirements[round-1]
        file = open("questions/"+file_path, "r")
        for line in file:
            questions.append(line.split("/"))
        file.close()
        select = np.random.randint(5)
        return questions[select]

    def load_user(save_file, user):
        print("Searching...")
        sleep(0.3)
        text = open(save_file, "r")
        for saved_user in text:
            saved_user = saved_user.split("/")
            if user == saved_user[0]:
                return game(int(saved_user[1]), int(saved_user[2]))
        text.close()
        exit("User not found")

