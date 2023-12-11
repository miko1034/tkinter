from tkinter import *


def button_clicked():
    entered_text = entry1.get()
    
    output_text.delete(0.0,END)
    manipulated_text = "You just typed in: " + entered_text
    output_text.insert(END,manipulated_text)

#window
window = Tk()

#title
window.title("My First Gui!")

#label
label = Label(window, text="Enter something below: ").grid(row=0,column=0,sticky=W)

#input box
entry1 = Entry(window, width=20,bg="light blue")
entry1.grid(row=1,column=1,columnspan=2,sticky=W)

#output text
output_text = Text(window,width=75,height=6, wrap=WORD,background="light blue")
output_text.grid(row=3,column=0,columnspan=2,sticky=W)

#button
button = Button(window,text="Sumbmit",width=5,command=button_clicked).grid(row=2,column=0,sticky=W)



window.mainloop()

