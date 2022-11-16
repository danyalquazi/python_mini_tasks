from tkinter import *

root = Tk()

def left_click(event):
    print("You clicked left mouse Button")

def mid_click(event):
    print("You clicked the wheel")

def right_click(event):
    print("You clicked the right mouse key")

mainl= Label(root, text="Click any button of your mouse anywhere in this window", bg= "black", fg = "white")
mainl.pack(fill=X)

f1 = Frame(root, width=350, height=250)

f1.bind("<Button-1>", left_click)
f1.bind("<Button-2>", mid_click)
f1.bind("<Button-3>", right_click)

f1.pack()

root.mainloop()
