
FILE_SAVE = "save/save.txt"
FILE_LEGEND = "save/legend.txt"

class Saver:
    def __init__(
        self,
        actual_game,
        #if file = save, it will save on save.txt other will save on legend.txt
        file="save.txt",
    ):
        if file == 'save.txt':
            file = FILE_SAVE
        else:
            file = FILE_LEGEND
        text = open(file, 'a')
        new_user = [actual_game.username, str(actual_game.get_round()), str(actual_game.get_cash())]
        text.write("/".join(new_user)+'\n')
        text.close()

    def validate_user(user):
        users = open(FILE_SAVE, "r")
        for line in users:
            line = line.split('/')
            if line[0] == user:
                print("User already registered")
                return 'registered'
        return 'not registered'
    

