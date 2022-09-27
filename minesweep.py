from tkinter import *
import settings
import utils
import images
from cell import Cell

# Creating the window itself
root = Tk()
root.configure(bg="white")                              # bg = background
root.geometry(f"{settings.width}x{settings.height}")    # The size
root.resizable(False, False)
root.title('MineSweeper.exe')

# Creating the frames
top_frame = Frame(                  # creating Frame that should contain restart, time & score
    root,                           # what element are we placing the frame in
    bg="gray",
    width=settings.width-6,         # the width is 300, so it lines up with the window
    height=utils.height_pro(18)
)
bottom_frame = Frame(
    root,
    bg="red",
    width=settings.width-6,
    height=utils.height_pro(80)-6
)

# placing frames
top_frame.place(x=3, y=0)
bottom_frame.place(x=3, y=utils.height_pro(20)+3)


flag = PhotoImage(file=r"C:\Users\gusta\PycharmProjects\Minesweeper-test\images\flag.png")
cell = PhotoImage(file=r"C:\Users\gusta\PycharmProjects\Minesweeper-test\images\cell.png")
mine = PhotoImage(file=r"C:\Users\gusta\PycharmProjects\Minesweeper-test\images\mine.png")

img = [cell, flag, mine]

# Creating minefield



for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_button(
            bottom_frame,
            img[0]
        )
        c.cell_button.grid(
            column=x, row=y
        )



Cell.randomize_mines()
print(Cell.all)


root.mainloop()                     # Run until close
