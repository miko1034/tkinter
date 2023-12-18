from tkinter import *

def collectdata():
    name = nameinput.get()
    surname = surnameinput.get()
    age = ageVar.get()
    selectedgender = genderVar.get()
    hobby = hobbyinput.get()
    data = {"name":name,"surname":surname,"age":age,"selectedgender":selectedgender,"hobby":hobby}
    print(data)

###creation of window
window = Tk()
window.title("Questionaire")
window.geometry("400x500")

###making frames
lframe= Frame(window,bg="black",highlightbackground="white",highlightthickness=2)
rframe= Frame(window,bg="black",highlightbackground="white",highlightthickness=2)
titleframe = Frame(window,bg="black",highlightbackground="white",highlightthickness=2)


###creation of objects

##for title frame
title = Label(titleframe,text="My Questionaire",bg="black",fg="white",font=("Rethink Sans",20))
title.place(x=95,y=13)

##for left side frame
#name
namelabel = Label(lframe,text="Name:",bg="black",fg="white",font=("Rethink Sans", 12))
namelabel.place(x=25,y=10)
#surname
surnamelabel = Label(lframe,text="Surname:",bg="black",fg="white", font=("Rethink Sans", 12))
surnamelabel.place(x=25,y=50)
#age
agelabel = Label(lframe,text="Age:",bg="black",fg="white", font=("Rethink Sans", 12))
agelabel.place(x=25,y=90)
#hobby
hobbylabel = Label(lframe,text="Your Hobby:",bg="black",fg="white", font=("Rethink Sans", 12))
hobbylabel.place(x=25,y=130)
#gender
genderlabel = Label(lframe,text="Your Gender:",bg="black",fg="white", font=("Rethink Sans", 12))
genderlabel.place(x=25,y=250)

##for right side frame
#name
nameinput = Entry(rframe,bg="#262626",fg="white",font=("Rethink Sans", 12),highlightbackground="white",highlightthickness=1)
nameinput.place(x=23,y=10)
#surname
surnameinput = Entry(rframe,bg="#262626",fg="white",font=("Rethink Sans", 12),highlightbackground="white",highlightthickness=1)
surnameinput.place(x=23,y=50)
#age
ageVar = IntVar()
agespin = Spinbox(rframe,textvariable=ageVar,from_=1,to=100,width=5,bg="#262626",fg="white",font=("Rethink Sans", 12),highlightbackground="white",highlightthickness=1)
agespin.place(x=23,y=90)  
#hobby
hobbyinput = Entry(rframe,bg="#262626",fg="white",font=("Rethink Sans", 12),highlightbackground="white",highlightthickness=1)
hobbyinput.place(x=23,y=130,width=190,height=100)
#gender
genderVar= StringVar()
genderrb = Radiobutton(rframe, text="Male", variable=genderVar, value="male",bg="#262626",fg="#808080",font=("Rethink Sans", 12),highlightbackground="white",highlightthickness=1)
genderrb.place(x=23,y=250)
rb = Radiobutton(rframe,text="Female", variable=genderVar,value="female",bg="#262626",fg="#808080",font=("Rethink Sans", 12),highlightbackground="white",highlightthickness=1)
rb.place(x=23,y=290)
#submit
submit = Button(rframe,text="Submit",command=collectdata,width=17,bg="#262626",fg="white",font=("Rethink Sans", 12),highlightbackground="white",highlightthickness=1)
submit.place(x=23,y=370)

###packing of frames
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