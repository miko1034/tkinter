from tkinter import *

x=10
y=10
a=50
b=50
x_vel = 5
y_vel = 5

def on_keypress():
    pass
def on_keyrelease():
    pass

def move():
    global x
    global y
    global x_vel
    global y_vel
    if x<0:
        x_vel = 5
    if x > 350:
        x_vel = -5
    if y < 0:
        y_vel = 5
    if y > 250:
        y_vel = -5
    canvas1.move(circle,x_vel,y_vel)
    coordinates = canvas1.coords(circle)
    x = coordinates[0]
    y = coordinates[1]
    window.after(33,move)

#window
window = Tk()
window.geometry("400x300")
#mainframe
mainframe = Frame(window,bg="light gray")
#main canvas
canvas1 = Canvas(mainframe, height=400,width=400)
canvas1.place(x=0,y=0)
coord = [x,y,a,b]
circle = canvas1.create_oval(coord,outline="blue",fill="blue")

#packing
mainframe.pack()
mainframe.pack_propagate(False)
mainframe.configure(width=400,height=300)
#run

move()

window.bind_all("<KeyPress>",on_keypress)
window.bind_all("<KeyRelease>", on_keyrelease)

window.mainloop()