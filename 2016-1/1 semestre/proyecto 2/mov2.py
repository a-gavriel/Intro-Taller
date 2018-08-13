from tkinter import *

class App(object):
    def __init__(self, master, **kwargs):
        self.master=master
        master.bind('<KeyRelease>',self.release)
        master.bind('<Key>',self.press)
    def press(self,event):
        global puerta1 , puerta2 , puerta3 , puerta4 , puerta5 , puerta6
        if event.keysym=="1":
            print ("puerta1= False")
        elif event.keysym=="2":
            print ("puerta2= False")
        elif event.keysym=="3":
            print ("puerta3= False")
        elif event.keysym=="4":
            print ("puerta4= False")
        elif event.keysym=="5":
            print ("puerta5= False")
        elif event.keysym=="6":
            print ("puerta6= False")

                   
    def release(self,event):
        global puerta1 , puerta2 , puerta3 , puerta4 , puerta5 , puerta6 , jugador
        if event.keysym=="1":
            print ("puerta1= True")
        elif event.keysym=="2":
            print ("puerta2= True")
        elif event.keysym=="3":
            print ("puerta3= True")
        elif event.keysym=="4":
            print ("puerta4= True")
        elif event.keysym=="5":
            print ("puerta5= True")
        elif event.keysym=="6":
            print ("puerta6= True")

        
        
    


            
root=Tk()
app=App(root)
root.mainloop()
