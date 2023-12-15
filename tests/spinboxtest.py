from tkinter import * 

window = Tk()
window.geometry("300x300")

mainframe = Frame(window)

def on_click():
    num = v.get()
    textbox.delete(0.0,END)
    textbox.insert(END,num)
    pass




v=IntVar()
spin = Spinbox(mainframe,textvariable=v,from_=1,to=10)
spin.place(x=10,y=10)

textbox = Text(mainframe,width=20,height=10)
textbox.place(x=50,y=50)

button = Button(mainframe,width=10,text="submit",command=on_click)
button.place(x=100,y=250)


mainframe.pack(side=TOP)
mainframe.pack_propagate(False)
mainframe.configure(height=400,width=400)

window.mainloop()