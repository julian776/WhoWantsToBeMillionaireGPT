from dotenv import load_dotenv

load_dotenv(".env")

from app import Game, Saver, ScreenManager, GameManager, load_login_frame
import tkinter as tk
from tkinter import ttk
from questions import QuestionsRepository

# Create a Tkinter window
root = tk.Tk()
root.geometry("850x630")

style = ttk.Style(root)
style.theme_use("clam")

# Create frames
app = ttk.Frame(root)
app.pack()

actual_game = Game(1, 00, '')
question = None

repo = QuestionsRepository()

login_section = ttk.Frame(app)
load_login_frame(frame=login_section, game=actual_game)

login_section.pack()
login_section.wait_window()

question_section = ttk.Frame(app)

status_label = ttk.Label(root, text="")
status_label.pack()


def display_next_question():
    # Destroy to verify clean screen
    ScreenManager.clean(question_section)

    question = repo.get_questionLLM()
    print("question: ", question.question)

    ScreenManager.screen_updater(
        app,
        question_section,
        actual_game,
        status_label,
        question,
        check_answer,
    )


bottom_frame = ttk.Frame(app)
result_label = ttk.Label(bottom_frame)


def check_answer(a, b):
    print(a, b)
    if a == b:
        GameManager.next_round(actual_game)
        result_label.config(text="Correct!")
        root.after(2000, display_next_question)
    else:
        result_label.config(text="Incorrect.")


display_next_question()


def save_and_exit():
    Saver(actual_game, file="save.txt")
    exit("Saved succesful")


save_button = ttk.Button(
    bottom_frame,
    text="SAVE",
    command=lambda : Saver(actual_game, file="save.txt"),
)

finalize_button = ttk.Button(
    bottom_frame,
    text="FINALIZE",
    command=save_and_exit,
)

question_section.grid(row=3, column=2)
result_label.grid(row=7, column=2)
save_button.grid(row=8, column=1)
finalize_button.grid(row=8, column=2)
bottom_frame.grid(row=10, column=2)


root.mainloop()
