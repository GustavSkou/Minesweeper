import cell
from tkinter import *
import random

import settings


class Cell:
    all = []
    def __init__(self, x, y, is_mine=False, flaged=False):  # init meaning when it call apon it goes though it attibuts
        self.flaged = flaged
        self.is_mine = is_mine
        self.cell_button = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_button(self, location, img):
        button = Button(
            location,
            image=img,
            #text=f"{self.x},{self.y}",
            height=10,
            width=10
        )

        button.bind('<Button-1>', self.left_click)
        button.bind('<Button-3>', self.right_click)

        self.cell_button = button

    def left_click(self, event):
        if self.flaged:
            print("CELL FLAGGED")
        elif not self.is_mine:
            print("NOT MINE")
        else:
            print("BOOM")

    def right_click(self, event):
        if not self.flaged:
            self.flaged = True
            print("FLAGGED")

        else:
            self.flaged = False
            print("UNFLAGED")

    @staticmethod
    def randomize_mines():
        picked_mines = random.sample(Cell.all, settings.mines)
        print(picked_mines)
        for picked_mines in picked_mines:
            picked_mines.is_mine = True


    def __repr__(self):
        return f"Cell({self.x}, {self.y}, {self.is_mine})"
