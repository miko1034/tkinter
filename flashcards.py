from tkinter import *


def cpu():
    output_text.delete(0.0,END)
    newtext = "Some information about the CPU blah blah blah blah blah blah blah blah blah. Hi Mr Clark"
    output_text.insert(END,newtext)
    
def fde():
    pass

window = Tk()

window.title("Flashcards")
window.geometry("300x300")

#creation of the frame
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)


#The CPU
cpu_button = Button(frame1, text="The Cpu", command=cpu)#.pack(padx=40,pady=40,side=LEFT)
#cpu_button.grid(row=1,column=0,columnspan=3,sticky=W)

#The FDE Cycle
fde_button = Button(frame2, text="The FDE Cycle", command=fde)
#fde_button.grid(row=2,column=0,columnspan=3,sticky=W)

#Output text
output_text = Text(window, width=20,height=300,wrap=WORD,background="light blue")#.grid(row=10,column=10,columnspan=1,sticky=NE)

cpu_button.place(x=30,y=30)
fde_button.pack()
frame1.pack(padx=40,pady=40,side=TOP,anchor=NW)
frame2.pack(padx=40,pady=40,side=LEFT,anchor=W)
frame3.pack()
output_text.pack(padx=10,pady=10,side=RIGHT)

mainloop()