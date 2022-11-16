from tkinter import *
import tkinter.messagebox

root =Tk()

tkinter.messagebox.showinfo('My first title', 'Elephants can fly')

a = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if a == 'yes':
    print("I'll gift you a mirror")
else:
    print("Don't worry I'll never gift you a mirror")    

root.mainloop()
