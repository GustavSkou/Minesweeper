from tkinter import *

import settings
import utils

from cell import Cell
from restart import Restart


# Creating the window itself
win = Tk()
win.configure(bg="white")                              # bg = background
win.geometry(f"{settings.width}x{settings.height}")    # The size
win.resizable(False, False)
win.title('MineSweeper.exe')

# Creating the frames
top_frame = Frame(                  # creating Frame that should contain restart, time & score
    win,                           # what element are we placing the frame in
    bg="gray",
    width=settings.width-6,         # the width is 300, so it lines up with the window
    height=utils.height_pro(18)
)
bottom_frame = Frame(
    win,
    bg="red",
    width=settings.width-6,
    height=utils.height_pro(80)-6
)

# placing frames
top_frame.place(x=3, y=0)
bottom_frame.place(x=3, y=utils.height_pro(20))

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_button(
            bottom_frame,
            txt=""
        )
        c.cell_button.grid(
            column=x, row=y
        )


# Place restart button
r = Restart()
r.create_button(
    top_frame
)
r.restart_button.place(
    x=utils.width_pro(50)-3, y=utils.top_frame_height(50), anchor=CENTER
)

Cell.randomize_mines()

win.mainloop()                     # Run until close
