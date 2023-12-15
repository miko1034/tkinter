from tkinter import *

def onclick():
    c1 = var1.get()
    c2 = var2.get()
    c3 = var3.get()
    textbox.delete(0.0,END)
    textbox.insert(END,f"{c1}\n{c2}\n{c3}\n")


#making window
window = Tk()
window.geometry("300x300")

#making frame
mainframe = Frame(window)

#making variables for each checkbox state
var1=IntVar()
var2=IntVar()
var3=IntVar()
#making check boxes
cbox1 = Checkbutton(mainframe,text="Check box 1", variable=var1)
cbox1.place(x=10,y=10)
cbox2 = Checkbutton(mainframe,text="Check box 2",variable=var2)
cbox2.place(x=10,y=30)
cbox3= Checkbutton(mainframe,text="Check box 3", variable=var3)
cbox3.place(x=10,y=50)
#textbox
textbox = Text(mainframe, width=20,height=10)
textbox.place(x=10,y=70)
#button
submit = Button(mainframe,text="Submit", width=10,command=onclick)
submit.place(x=10,y=250)

#packing frames
mainframe.pack()
mainframe.pack_propagate(False)
mainframe.configure(width=300,height=300)

window.mainloop()