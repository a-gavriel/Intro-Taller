from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print (e.get())
    e.delete(0, END)

    
b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
