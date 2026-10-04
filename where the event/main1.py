from tkinter import*
from tkinter import messagebox

root= Tk()
root.geometry("200x300")


def msg():
    messagebox.showwarning("alert","Stop!Virus Found." )

button=Button(root,text="scan for Virus",command=msg)
button.place(x=40,y=80)

root.mainloop()
