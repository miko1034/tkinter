from tkinter import *

#creation of window
window = Tk()
window.title("Questionaire")
window.geometry("400x500")
#making frames
lsideframe= Frame(window,bg="gray")
rsideframe= Frame(window,bg="light gray")
titleframe = Frame(window,bg="light blue")
#creation of objects
title = Label(titleframe, )


#packing of frames
titleframe.pack(side=TOP)
lsideframe.pack(side=LEFT)
rsideframe.pack(side=RIGHT)
titleframe.pack_propagate(False)
lsideframe.pack_propagate(False)
rsideframe.pack_propagate(False)
titleframe.configure(height=60,width=400)
lsideframe.configure(height=500,width=150)
rsideframe.configure(height=500,width=250)

window.mainloop()