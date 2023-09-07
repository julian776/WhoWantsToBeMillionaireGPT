from time import sleep
from os import system, name
from tkinter import ttk

from questions.question import Question

class screen_manager:
    def show_question(frame, question: Question, check_answer):
        # Create a label to display the question
        question_label = ttk.Label(frame, text=question.question, wraplength=300)
        question_label.grid(row=2, column=2)

        # Create buttons for the multiple-choice options
        option_buttons = []
        row=3
        for i in ['a', 'b', 'c', 'd']:
            option_button = ttk.Button(frame, text=question.options[i], command= lambda a=i, b=question.answer: check_answer(a,b))
            option_buttons.append(option_button)
            option_button.grid(row=row, column=2)
            row+=1

    def screen_updater(frame_app, frame_question, manager, status_label, question, check_answer):
        round = manager.get_round()
        cash = manager.get_cash()
        info_text = str("\nRound " + str(round) + " Cash Earned " + str(cash) + "\n")
        status_label.config(text=info_text)
        screen_manager.show_question(frame_question, question, check_answer)

    def clean(frame):
        for widget in frame.winfo_children():
            widget.destroy()


    

        
    
    