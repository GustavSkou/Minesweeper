from tkinter import *

root = Tk()
root.configure(bg="white")                              # bg = background
root.geometry("200x200")    # The size
root.resizable(False, False)
root.title('MineSweeper.exe')

photo = PhotoImage(file=r"C:\Users\bruger\Desktop\Minesweeper-main\images\flag.png")
cell_img = photo.subsample(1, 1)

button = Button(
            image=cell_img,
            height=50,
            width=50
        )
button.place(
    x=0, y=0
)

root.mainloop()
