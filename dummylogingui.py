from tkinter import *

def loginsubmit():
    username = usernameinput.get()
    #i would put code to clear username but that usually doesnt happen on normal websites + its more convenient if it isnt cleared
    password = passwordinput.get()
    passwordinput.delete(0,END)
    print(f"THe username is {username} and the password is {password}")
    pass

#makeing the window
window = Tk()
window.resizable(False,False)
window.title("Login")
window.geometry("400x500")

#making the frames
titleframe = Frame(window,bg="#1a1a1a")
mainframe = Frame(window,bg="#333333")

#title
title = Label(titleframe,text="Enter Your Details:",bg="#1a1a1a", fg="white",font=("Rethink Sans",20))
title.place(x=83,y=36)
#login objects
#username
usernamelabel = Label(mainframe, text="Enter Username:", bg="#333333",fg="white",font=("Rethink Sans", 15))
usernamelabel.place(x=30,y=30)
usernameinput = Entry(mainframe,text="username",bg="#999999",fg="#000000",font=("Rethink Sans", 10))
usernameinput.place(x=30,y=70)
#password
passwordlabel = Label(mainframe,text="Enter Password:", bg="#333333", fg="white",font=("Rethink Sans",15))
passwordlabel.place(x=30,y=130)
passwordinput = Entry(mainframe,text="password",bg="#999999",fg="#000000",font=("Rethink Sans", 10))
passwordinput.place(x=30,y=170)
#submit
submit = Button(mainframe,text="Submit", bg="black",fg="white",font=("Rethink Sans", 10), command=loginsubmit)
submit.configure(width=40)
submit.place(x=30,y=300)

#carry on here with a pop up of some sorts or a label that tells the user
#their info has been collected or an error occured.

#packing of frames
titleframe.pack(side=TOP)
titleframe.pack_propagate(False)
titleframe.configure(height=100,width=400)

mainframe.pack(side=TOP)
mainframe.pack_propagate(False)
mainframe.configure(height=400,width=400)

#running the main loop
window.mainloop()