from tkinter import *

def something():
    print("yeah i am lazy person")

def Danyal():
    print("you just clicked Danyal")

def Quitfun():
    print("Just kidding \n Go press that red X")

root = Tk()

# ---------- Menu ----------

m1 = Menu(root)
root.config(menu=m1)

subm = Menu(m1)

m1.add_cascade(label="File", menu=subm)

subm.add_command(label="New project", command= something)
subm.add_command(label="New", command= something)
subm.add_separator()
subm.add_command(label="Quit", command= Quitfun)

subm1 = Menu(m1)
m1.add_cascade(label="Edit", menu=subm1)

subm1.add_command(label="Danyal", command= Danyal)
subm1.add_command(label="d1", command= Danyal)

# ---------- Toolbar ----------

toolbar = Frame(root, bg= "gray")

b1 = Button(toolbar,text="Tool 1",command= Danyal)
b1.pack(side=LEFT, padx=2, pady=2)

b2 = Button(toolbar,text="Tool 2", command= Danyal)
b2.pack(side=LEFT, padx=2, pady=2)

b3 = Button(toolbar,text="Tool 3", command= Danyal)
b3.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side = TOP, fill=X)

# ---------- Status Bar ----------

sbar = Label(root, text = "preparing to blow up your system...", bd = 2, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill=X)



root.mainloop()
