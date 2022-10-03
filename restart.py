from tkinter import Button
from cell import Cell

class Restart:
    def __init__(self):
        self.restart_button = None

    def create_button(self, location):
        button = Button(
            location,
            text="R",
            font=("Arial", "6"),
            height=1,
            width=1
        )

        button.bind('<Button-1>', self.left_click)
        self.restart_button = button

    def left_click(self, event):
        print("restart")
        Cell.clear_mines()
        Cell.randomize_mines()

