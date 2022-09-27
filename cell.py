from tkinter import *


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None

    def create_button(self, location, cell_img):
        button = Button(
            location,
            image=cell_img,
            height=10,
            width=10
        )
        self.cell_button = button
