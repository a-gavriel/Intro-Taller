import time
from tkinter import *
root = Tk()
root.title("Timer")
root.geometry("100x100")

def countdown(count):
    label = Label(root, text= count)
    label.place(x=35, y=15)

for i in range(2,0,-1):
    countdown(i)
    time.sleep(1)
    
countdown(2)

root.mainloop()
