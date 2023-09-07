from app import game
from app.saver import saver
from app.loaders import loaders
from app.screen_manager import screen_manager  # Easy notation
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
from questions.questions_repository import QuestionsRepository

load_dotenv("./.env")

QUESTIONS = ["questions1.txt", "questions2.txt", "questions3.txt", "questions4.txt", "questions5.txt"]
SAVE_FILE = "save/save.txt"

# Create a Tkinter window
root = tk.Tk()
root.geometry("850x630")

style = ttk.Style(root)
style.theme_use("clam")

# Create frames
app = ttk.Frame(root)
question_section = ttk.Frame(app)

status_label = ttk.Label(root, text="")
status_label.pack()

actual_game = game.game(1, 00)
question = None

repo = QuestionsRepository()
def display_next_question():
    result_label.config(text="")
    question = repo.get_questionLLM()
    print("question: ", question)
    screen_manager.screen_updater(app, question_section, actual_game, status_label, question, check_answer)

result_label = ttk.Label(question_section)
def check_answer(a, b):
    print(a, b)
    if a == b:
        game.game_manager.next_round(actual_game)
        result_label.config(text="Correct!")
        root.after(2000, display_next_question)
    else:
        result_label.config(text="Incorrect.")
    result_label.grid(row=7, column=2)

display_next_question()

app.pack()
question_section.pack()

root.mainloop()
