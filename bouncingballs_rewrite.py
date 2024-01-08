from tkinter import *

mcoord = [10,10,50,50]
scoord = [10,10,75,75]

def movemainball():
    pass

#window
window = Tk()
window.title("Balls")
window.geometry("500x300")

#frames
sideframe = Frame(bg="light blue")
mainframe = Frame(bg="gray")

#creating canvases
sidecanvas = Canvas(sideframe, width=100,height=300,bg="green")
maincanvas = Canvas(mainframe,width=400, height=300,bg="blue")
sidecanvas.place(x=0,y=0)
maincanvas.place(x=0,y=0)

#creating circles
maincircle = maincanvas.create_oval(mcoord,outline="red",fill="red")
sidecircle = sidecanvas.create_oval(scoord,outline="blue",fill="blue")

#packing of frames
mainframe.pack(side=RIGHT)
mainframe.pack_propagate(False)
mainframe.configure(width=400,height=300)
sideframe.pack(side=LEFT)
sideframe.pack_propagate(False)
sideframe.configure(width=100,height=300)

movemainball()

window.mainloop()