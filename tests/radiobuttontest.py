from tkinter import *

def onclick():
    rselected = rbvar.get()
    textbox.delete(0.0,END)
    textbox.insert(END,rselected)

#creating window
window = Tk()
window.geometry("300x300")
window.title("TEST")

#creating frame
mainframe = Frame(window)

#radiobuttons
rbvar = IntVar()
rb = Radiobutton(mainframe, text="one", variable=rbvar,value=1)
rb.place(x=10,y=10)
rb = Radiobutton(mainframe,text="two", variable=rbvar,value=2)
rb.place(x=10,y=30)
#textbox
textbox = Text(mainframe,width=20,height=10)
textbox.place(x=10,y=50)
#button
button = Button(mainframe, width=10,text="Submit", command=onclick)
button.place(x=10,y=240)

#packing of frames
mainframe.pack()
mainframe.pack_propagate(False)
mainframe.configure(height=300,width=300)


window.mainloop()