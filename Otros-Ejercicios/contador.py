
import tkinter
import sys

root = tkinter.Tk()
root.geometry("200x150")
root.title("RUNS")

counter = tkinter.IntVar()

def onClick(event=None):
    counter.set(counter.get() + 1)

tkinter.Label(root, textvariable=counter,font=("Helvetica", 30)).pack()
tkinter.Button(root, text="\n  Increase  \n", command=onClick, fg="dark green", bg = "white").pack()

root.mainloop()
