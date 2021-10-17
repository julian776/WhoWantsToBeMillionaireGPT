from time import sleep
from app.saver import saver
from app.screen_manager import screen_manager

class game:
    def __init__(self, round, cash):
        self._round = round
        self._cash = cash

    def get_cash(self):
        return self._cash

    def get_round(self):
        return self._round

class game_manager(game):
    def next_round(actual_game):
        multiplier = 1750
        if actual_game.get_round() == 5:
            multiplier = 34589
        cash = (actual_game.get_round())*multiplier
        actual_game._round += 1
        actual_game._cash += cash
        screen_manager.clean()
        print("\n\n  Earned ", cash)
        sleep(1.2)
        screen_manager.clean()

    def validate_answer(actual_game, answer, question, user):
        if answer == question[5][0]:
            game_manager.next_round(actual_game)
        elif answer == "save":
            saver(actual_game, user, file="save.txt")
            exit("Saved succesful")
        else: 
            screen_manager.clean()
            sleep(0.55)
            saver(actual_game, user, file="legend.txt")
            exit('\n\n  Game Over')
    
    

        

