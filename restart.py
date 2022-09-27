from tkinter import Button


class Restart:
    def __init__(self):
        self.restart_button = None

    def create_button(self, location, img):
        button = Button(
            location,
            image=img,
            height=10,
            width=10
        )

        button.bind('<Button-1>', self.left_click)
        self.restart_button = button


    def left_click(self, event):
        print("restart")
