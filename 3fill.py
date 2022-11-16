from tkinter import *

root = Tk()

button1 = Button(root, text="without fill", bg="Black", fg="white")
button1.pack()
button2 = Button(root, text="Fil X axis", bg="green", fg="white")
button2.pack(fill =X,side= 'bottom')

root.mainloop()
