from tkinter import *

class my_buttons(object):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printbutton = Button(frame, text="print something", command=self.funp)
        self.printbutton.pack(side=LEFT)

        self.quitbutton = Button(frame, text="Quit this crap", command =frame.quit)
        self.quitbutton.pack(side=LEFT)

    def funp(self):
        print("WOW, this thing actually works!!!")




root = Tk()
obj = my_buttons(root)
root.mainloop()
