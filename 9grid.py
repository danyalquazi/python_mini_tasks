from tkinter import *

root=Tk()

n_label = Label(root, text ="Name")
p_label = Label(root, text ="Password")

n_entry = Entry(root)
p_entry = Entry(root)

n_label.grid(row=0)
p_label.grid(row=1)

n_entry.grid(row=0, column=1)
p_entry.grid(row=1, column=1)

s_button = Button(root, text = "Submit", bg="gray", fg ="white")
s_button.grid(columnspan=2)

root.mainloop()
