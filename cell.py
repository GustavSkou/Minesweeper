import cell
from tkinter import *
import settings
import random



class Cell:
    all = []
    bottom = []
    top = []
    left = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    right = [72, 73, 74, 75, 76, 77, 78, 79, 80]
    color = ["white", "#58c437", "#d1c75a", "#3db6d4", "#b88400", "#2357cf", "#e08be8", "#922abf", "#755734", ]
            #           green,     yellow    orange    light blue    blue      pink       purple     brown

    for pos in range(81):
        if (pos - 8) % 9 == 0:  # bottom
            bottom.append(pos)
        if pos % 9 == 0:
            top.append(pos)  # top

    def __init__(self, x, y, is_mine=False, flagged=False):  # init meaning when it's called apon it goes though it attibuts
        self.flagged = flagged
        self.is_mine = is_mine
        self.cell_button = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_button(self, location, img):
        button = Button(
            location,
            image=img,
            bg="gray",
            height=10,
            width=10
        )

        button.bind('<Button-1>', self.left_click)
        button.bind('<Button-3>', self.right_click)

        self.cell_button = button

    def left_click(self, event):
        if self.flagged:
            print("CELL FLAGGED")
        elif not self.is_mine:  # When we click on a cell that isn't a mine
            mine_count = 0
            pos = Cell.all.index(self)
            mine_detector = []      #We cannot add the cells at the start if so we can get an out-of-bounds error :(
            if pos == 0:
                mine_detector = [
                    Cell.all[1],
                    Cell.all[9],
                    Cell.all[10]
                ]
            elif pos == 8:
                mine_detector = [
                    Cell.all[7],
                    Cell.all[16],
                    Cell.all[17]
                ]
            elif pos == 72:
                mine_detector = [
                    Cell.all[63],
                    Cell.all[64],
                    Cell.all[73]
                ]
            elif pos == 80:
                mine_detector = [
                    Cell.all[70],
                    Cell.all[71],
                    Cell.all[79]
                ]
            else:
                for item in Cell.left:
                    if pos == item:
                        mine_detector = [
                            Cell.all[pos - 1],      # left
                            Cell.all[pos + 1],
                            Cell.all[pos + 8],
                            Cell.all[pos + 9],
                            Cell.all[pos + 10]
                        ]
                for item in Cell.right:
                    if pos == item:
                        mine_detector = [
                            Cell.all[pos - 10],         # right
                            Cell.all[pos - 9],
                            Cell.all[pos - 8],
                            Cell.all[pos - 1],
                            Cell.all[pos + 1]
                        ]
                for item in Cell.top:
                    if pos == item:
                        mine_detector = [
                            Cell.all[pos - 9],          # top
                            Cell.all[pos - 8],
                            Cell.all[pos + 1],
                            Cell.all[pos + 9],
                            Cell.all[pos + 10]
                        ]
                for item in Cell.bottom:
                    if pos == item:
                        mine_detector = [
                            Cell.all[pos - 10],         # bottom
                            Cell.all[pos - 9],
                            Cell.all[pos - 1],
                            Cell.all[pos + 8],
                            Cell.all[pos + 9],
                        ]
            if not mine_detector:               # if the list is empty
                mine_detector = [
                    Cell.all[pos - 10],
                    Cell.all[pos - 9],
                    Cell.all[pos - 8],
                    Cell.all[pos - 1],
                    Cell.all[pos + 1],
                    Cell.all[pos + 8],
                    Cell.all[pos + 9],
                    Cell.all[pos + 10]
                ]
            for item in mine_detector:
                if item.is_mine:
                    mine_count = mine_count + 1

            self.cell_button.configure(bg=Cell.color[mine_count])

            print(pos)
            print(mine_detector)
            print(mine_count)
        else:
            self.mine()

    def right_click(self, event):
        if not self.flagged:
            self.flagged = True
            print("FLAGGED")
            self.flag()
        else:
            self.flagged = False
            print("UNFLAGGED")
            self.cell_color()

    def mine(self):         # to show mine
        self.cell_button.configure(bg="black")

    def flag(self):         # to show flag
        self.cell_button.configure(bg="#b52a2a")

    def cell_color(self):
        self.cell_button.configure(bg="gray")

    @staticmethod
    def clear_mines():
        for item in Cell.all:
            item.is_mine = False
            item.bg = "gray"

    @staticmethod
    def randomize_mines():
        picked_mines = random.sample(Cell.all, settings.mines)
        print(len(picked_mines), end=" ")
        print("mines", end=" ")
        print(picked_mines)
        for picked_mines in picked_mines:
            picked_mines.is_mine = True

    def __repr__(self):
        return f"Cell({self.x + 1}, {self.y + 1}, {self.is_mine})"
