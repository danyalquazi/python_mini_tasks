from tkinter import *

root = Tk()

button1 = Button(root, text="Button1", fg = "red")
button2 = Button(root, text="Button2", fg = "red")
button3 = Button(root, text="Button3", fg = "red")
button4 = Button(root, text="Button4", fg = "blue")
button1.pack(side= LEFT)
button2.pack(side= LEFT)
button3.pack(side= LEFT)
button4.pack(side= BOTTOM)


root.mainloop()
