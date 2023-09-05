from app import game
from app.saver import saver
from app.loaders import loaders
from app.screen_manager import screen_manager  # Easy notation
import tkinter as tk
from dotenv import load_dotenv
from questions.questions_repository import QuestionsRepository

load_dotenv()

QUESTIONS = ["questions1.txt", "questions2.txt", "questions3.txt", "questions4.txt", "questions5.txt"]
SAVE_FILE = "save/save.txt"

# Create a Tkinter window
root = tk.Tk()
root.geometry("800x600")

# Create frames
app = tk.Frame(root)
question_section = tk.Frame(app)

status_label = tk.Label(root, text="")
status_label.pack()

answer_entry = tk.Entry(root, width=30)
answer_entry.pack()

actual_game = game.game(1, 00)
question = None

repo = QuestionsRepository()
def display_next_question():
    question = repo.get_questionChatGPT()
    print("question: ", question)
    screen_manager.screen_updater(app, question_section, actual_game, status_label, question, check_answer)

def check_answer(a, b):
    print(a, b)
    result_label = tk.Label(question_section)
    if a == b:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect.", fg="red")
    result_label.grid(row=7, column=2)

    root.after(2000, display_next_question)

display_next_question()

app.pack()
question_section.pack()

# Start the Tkinter event loop
root.mainloop()
