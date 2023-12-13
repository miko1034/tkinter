from tkinter import *


def cpu():
    print("Cpu pressed")
    info.configure(text="Some information about the CPU blah blah blah blah blah blah blah blah blah. Hi Mr Clark")
    info.update()

def fde():
    print("Fde pressed")
    info.configure(text="Some informnation about the FDE cycle and stuff blah blah blah. Hello Mrs Brant")
    info.update()

def memory():
    print("memory")
    info.configure(text="Here is some more information about computer Memory and stuff. Like it just remembers thing and you dont need to know more. It has some 'cash' or 'cache' idk how its spelt but yeah it has that so its rather wealthy.")
    info.update()


#creation of window
window = Tk()
window.resizable()
window.title("Flashcards")
window.geometry("400x400")

#creation of frames
sidebutton_frame = Frame(window,bg="light blue")
main_frame = Frame(window,highlightbackground="black",highlightthickness=1)


#text
info = Label(main_frame,height=400,width=300,fg="black",text="test",bg="#A0E0F0",justify=LEFT,wraplength=300)
info.place(x=0,y=0)

#buttons
cpu_button = Button(sidebutton_frame, text="The Cpu", command=cpu)
cpu_button.place(x=20,y=10)
fde_button = Button(sidebutton_frame, text="FDE Cycle", command=fde)
fde_button.place(x=20,y=60)
memory_button = Button(sidebutton_frame, text="Memory", command=memory)
memory_button.place(x=20,y=110)

info.pack()


#frame configurations
sidebutton_frame.pack(side=LEFT)
sidebutton_frame.pack_propagate(False)
sidebutton_frame.configure(height=400,width=100)

main_frame.pack(side=RIGHT)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=300)

mainloop()