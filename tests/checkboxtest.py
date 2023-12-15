from tkinter import *

window = Tk()
window.geometry("300x300")

mainframe = Frame(window)

var1=IntVar()
var2=IntVar()
var3=IntVar()
cbox1 = Checkbutton(window,text="Check box 1", variable=var1)



mainframe.pack()
mainframe.pack_propagate(False)
mainframe.configure(width=300,height=300)