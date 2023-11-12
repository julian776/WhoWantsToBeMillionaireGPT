from time import sleep
from app.saver import Saver
from .screen_manager import ScreenManager

class Game:
    def __init__(self, round, cash, username):
        self._round = round
        self._cash = cash
        self.username = username

    def get_cash(self):
        return self._cash

    def get_round(self):
        return self._round

class GameManager(Game):
    def next_round(actual_game):
        multiplier = 1750
        if actual_game.get_round() == 5:
            multiplier = 34589
        cash = (actual_game.get_round())*multiplier
        actual_game._round += 1
        actual_game._cash += cash

    def validate_answer(self, actual_game, answer, question, user):
        if answer == question[5][0]:
            self.next_round(actual_game)
        elif answer == "save":
            Saver(actual_game, user, file="save.txt")
            exit("Saved succesful")
        else: 
            ScreenManager.clean()
            sleep(0.55)
            Saver(actual_game, user, file="legend.txt")
            exit('\n\n  Game Over')
    
    

        

