from tkinter import *

#makeing the window
window = Tk()
window.resizable(False,False)
window.title("Login")
window.geometry("400x500")

#making the frames
titleframe = Frame(window,bg="gray")
mainframe = Frame(window,bg="light blue")


#packing of frames
titleframe.pack(side=TOP)
titleframe.pack_propagate(False)
titleframe.configure(height=100,width=400)

mainframe.pack(side=TOP)
mainframe.pack_propagate(False)
mainframe.configure(height=400,width=400)


window.mainloop()