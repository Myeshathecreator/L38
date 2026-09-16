from tkinter import *

root=Tk()
root.title("Number pad")
root.geometry("300x400")

nums=[[9,8,7],[6,5,4],[3,2,1],['#', 0, '*']]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=95)
    root.rowconfigure(i, weight=1, minsize=70)
    for j in range(0,3):
        frame=Frame(master=root, relief=RAISED, borderwidth=1)

        frame.grid(row=i, column=j)
        label=Label(master=frame, text=nums[i][j], bg="#8ec7e3")
        label.pack(padx=5, pady=5)

root.mainloop()