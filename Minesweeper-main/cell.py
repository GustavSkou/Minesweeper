from tkinter import *
import settings
import utils


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None

    def create_button(self, location):
        photo = PhotoImage(file=r"C:\Users\bruger\Desktop\Minesweeper-main\images\flag.png")
        cell_img = photo.subsample(1, 1)
        button = Button(
            location,
            image=cell_img,
            height=10,
            width=10
        )
        self.cell_button = button
