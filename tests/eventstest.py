from tkinter import *

x=10
y=10
a=50
b=50
x_vel = 5
y_vel = 5
key_down = False

def on_keypress(event):
    global key_down
    global x_vel
    global y_vel
    if event.keysym == "Left":
        key_down = True
        x_vel = -5
        y_vel = 0
    if event.keysym == "Right":
        key_down = True
        x_vel = 5
        y_vel = 0
    if event.keysym == "Up":
        key_down = True
        x_vel = 0
        y_vel = -5
    if event.keysym == "Down":
        key_down = True
        x_vel = 0
        y_vel = 5
    
def on_keyrelease():
    global key_down
    key_down = False

def move():
    global x_vel
    global y_vel
    global key_down
    if key_down == True:
        canvas1.move(circle, x_vel,y_vel)
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