from app import game
from app.screen_manager import screen_manager  # Easy notation
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
from questions.questions_repository import QuestionsRepository

load_dotenv("./.env")

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
    # Destroy to verify clean screen
    screen_manager.clean(question_section)
    question = repo.get_questionLLM()
    print("question: ", question.question)
    screen_manager.screen_updater(app, question_section, actual_game, status_label, question, check_answer)


result_frame = ttk.Frame(app)
result_label = ttk.Label(result_frame)
result_label.grid(row=7, column=2)
def check_answer(a, b):
    print(a, b)
    if a == b:
        game.game_manager.next_round(actual_game)
        result_label.config(text="Correct!")
        root.after(2000, display_next_question)
    else:
        result_label.config(text="Incorrect.")

display_next_question()

app.pack()
question_section.pack()
result_frame.pack()

root.mainloop()
