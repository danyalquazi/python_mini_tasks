from tkinter import *

root = Tk()

def name():
    print("Hey!!! My name is Danyal :)")

n_button = Button(root, text ="Click me", command=name)
n_button.pack()

root.mainloop()
