
from tkinter import ttk
from time import sleep

from app import ScreenManager, Game

class Loaders:
    def load_menu():
        print("To start a new game type 0")
        print("Load a game type 1")
        request = input("Type what you would like to do: ")
        return request

    def load_user(
              frame: ttk.Frame,
                user,
                info_label: ttk.Label,
                game: Game
                ):
        print("Searching...")
        sleep(0.3)
        with open('./save/save.txt', "r") as text:
            print('user: ', user)
            for saved_user in text:
                print(saved_user)
                saved_user = saved_user.split("/")
                if user == saved_user[0]:
                    print('ACA')
                    frame.destroy()
                    game._round = int(saved_user[1])
                    game._cash = int(saved_user[2])
                    game.username = saved_user[0]
                
        info_label.config(text="User not found.")  
        frame.destroy()
        game._round = 0
        game._cash = 0
        game.username = user

def load_login_frame(frame, game):
        username_label = ttk.Label(frame, text="Username:")
        username_label.grid(row=0, column=0, padx=5, pady=5)

        username_entry = ttk.Entry(frame)
        username_entry.grid(row=0, column=1, padx=5, pady=5)

        info_label = ttk.Label(frame)
        info_label.grid(row=1, column=1)

        login_button = ttk.Button(
             frame,
               text="Login",
                 command=lambda : Loaders.load_user(frame, username_entry.get(), info_label, game))
        login_button.grid(row=2, column=0, columnspan=2, pady=10)



