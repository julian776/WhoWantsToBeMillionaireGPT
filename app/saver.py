
FILE_SAVE = "save/save.txt"
FILE_LEGEND = "save/legend.txt"

class saver:
    def __init__(self, actual_game, user, file="save.txt"): #if file = save, it will save on save.txt other will save on legend.txt
        if file == 'save.txt':
            file = FILE_SAVE
        else:
            file = FILE_LEGEND
        text = open(file, 'a')
        new_user = [user, str(actual_game.get_round()), str(actual_game.get_cash())]
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
    

