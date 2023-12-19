from tkinter import *

mcoord = [10,10,50,50]
scoord = [10,10,75,75]

def move(mx,my,mx_vel,my_vel,sx,sy,sx_vel,sy_vel):
    if sx<0:
        sx_vel = int(sx_vel + (2*sx_vel))
    if sx> 350:
        sx_vel = int(sx_vel - (2*sx_vel))
    if sy < 0:
        sy_vel = int(sx_vel + (2*sy_vel))
    if sy > 250:
        sy_vel = int(sy_vel - (2*sy_vel))
    sidecanvas.move(sidecanvas,sx_vel,sy_vel)
    scoordinates = sidecanvas.coords(sidecircle)
    sx = scoordinates[0]
    sy = scoordinates[1]
    if mx<0:
        mx_vel = int(mx_vel + (2*mx_vel))
    if mx> 350:
        mx_vel = int(str("-{mx_vel}"))
    if my < 0:
        my_vel = int(my_vel + (2*my_vel))
    if my > 250:
        my_vel = int(str("-{my_vel}"))
    maincanvas.move(maincircle,mx_vel,my_vel)
    mcoordinates = maincanvas.coords(maincircle)
    mx = mcoordinates[0]
    my = mcoordinates[1]
    window.after(33,move)

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

move(mcoord[0],mcoord[1],mcoord[2],mcoord[3],scoord[0],scoord[1],scoord[2],scoord[3])


window.mainloop()