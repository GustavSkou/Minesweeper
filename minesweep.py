import tkinter
from tkinter import *
import settings
import utils
from cell import Cell

# Creating the window itself
root = Tk()
root.configure(bg="white")                              # bg = background
root.geometry(f"{settings.width}x{settings.height}")    # The size
root.resizable(False, False)
root.title('MineSweeper.exe')

top_frame = Frame(                  # creating Frame that should contain restart, time & score
    root,                           # what element are we placing the frame in
    bg="gray",
    width=settings.width-6,         # the width is 300, so it lines up with the window
    height=utils.height_pro(20)
)

bottom_frame = Frame(
    root,
    bg="red",
    width=settings.width-6,
    height=utils.height_pro(80)-6
)

top_frame.place(x=3, y=0)           # We then place our frame in the top right for the window
bottom_frame.place(x=3, y=utils.height_pro(20)+3)

for x in range(13):
    for y in range(10):
        c = Cell()
        c.create_button(bottom_frame)
        c.cell_button.grid(
            column = y, row=x
        )

root.mainloop()                     # Run until close
