from tkinter import *

#creation of window
window = Tk()
window.title("Questionaire")
window.geometry("400x500")
#making frames
lframe= Frame(window,bg="gray")
rframe= Frame(window,bg="light gray")
titleframe = Frame(window,bg="light blue",highlightbackground="black",highlightthickness=2)
###creation of objects
#for title frame
title = Label(titleframe,text="My Questionaire",bg="light blue",font=("Rethink Sans",20))
title.place(x=95,y=13)
#for left side frame
namelabel = Label(lframe,text="Name:",bg="light blue",font=("Rethink Sans", 12))
namelabel.place(x=25,y=10)
surnamelabel = Label(lframe,text="Surname:",bg="light blue", font=("Rethink Sans", 12))
surnamelabel.place(x=25,y=50)
agelabel = Label(lframe,text="Age:",bg="light blue", font=("Rethink Sans", 12))
agelabel.place(x=25,y=90)
hobbylabel = Label(lframe,text="Your Hobby:",bg="light blue", font=("Rethink Sans", 12))
hobbylabel.place(x=25,y=130)
genderlabel = Label(lframe,text="Your Gender:",bg="light blue", font=("Rethink Sans", 12))
genderlabel.place(x=25,y=250)

#packing of frames
titleframe.pack(side=TOP)
lframe.pack(side=LEFT)
rframe.pack(side=RIGHT)
titleframe.pack_propagate(False)
lframe.pack_propagate(False)
rframe.pack_propagate(False)
titleframe.configure(height=60,width=400)
lframe.configure(height=500,width=150)
rframe.configure(height=500,width=250)

window.mainloop()