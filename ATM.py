from tkinter import *

root = Tk()
root.title("ATM machine")
root.geometry("400x400")

frame = Frame(master=root, relief=RIDGE, borderwidth=1, height=200, width=360, bg="#e38eb3")

lb1=Label(frame, text="Full Name", bg="#67042f", fg="white", width=12)

lb2=Label(frame, text="Email Id", bg="#67042f", fg="white", width=12)

lb3=Label(frame, text="Password", bg="#67042f", fg="white", width=12)

name=Entry(frame)
email=Entry(frame)
password=Entry(frame, show="*")

def display():
    n=name.get()
    greet="Hey, " + n + "!"
    message="\nCongratulations! You have successfully set \nyour pin."
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox=Text(bg="#FBC9DF",fg='black')

btn=Button(text="Set pin", bg="#07e5f9", fg="black", command=display)

frame.place(x=20, y=0)

lb1.place(x=20, y=20)
name.place(x=150, y=20)

lb2.place(x=20, y=80)
email.place(x=150, y=80)

lb3.place(x=20, y=140)
password.place(x=150, y=140)

btn.place(x=150, y=210)
textbox.place(y=250)

root.mainloop()