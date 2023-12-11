from tkinter import *

window = Tk()
window.title("Flashcards")
window.geometry("300x300")


for i in range(15):
    for j in range(15):
        frame = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()


window.mainloop()