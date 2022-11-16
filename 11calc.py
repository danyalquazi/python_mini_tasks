from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator =""
    text_input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

root = Tk()

root.title("DQ's Calculator")

operator=""
text_input = StringVar()

# ---------- Display ----------

display = Entry(root, font=('arial', 20, 'bold'), textvariable=text_input, bd = 20,
                    insertwidth= 3, bg ="black", fg = "white", justify = "right")
display.grid(columnspan=4)

# ---------- Row 1 ----------

b7 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="7", command = lambda:btnClick(7))
b7.grid(row=1, column=0)

b8 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="8", command = lambda:btnClick(8))
b8.grid(row=1, column=1)

b9 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="9", command = lambda:btnClick(9))
b9.grid(row=1, column=2)

b_add = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="+", command = lambda:btnClick("+"))
b_add.grid(row=1, column=3)

# ---------- Row 2 ----------

b4 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="4", command = lambda:btnClick(4))
b4.grid(row=2, column=0)

b5 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="5", command = lambda:btnClick(5))
b5.grid(row=2, column=1)

b6 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="6", command = lambda:btnClick(6))
b6.grid(row=2, column=2)

b_sub = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="-", command = lambda:btnClick("-"))
b_sub.grid(row=2, column=3)

# ---------- Row 3 ----------

b1 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="1", command = lambda:btnClick(1))
b1.grid(row=3, column=0)

b2 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="2", command = lambda:btnClick(2))
b2.grid(row=3, column=1)

b3 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="3", command = lambda:btnClick(3))
b3.grid(row=3, column=2)

b_mul = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="X", command = lambda:btnClick("*"))
b_mul.grid(row=3, column=3)

# ---------- Row 4 ----------

b_div = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="/", command = lambda:btnClick("/"))
b_div.grid(row=4, column=3)

b_clr = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="Clr", command = btnClear)
b_clr.grid(row=4, column=0)

b0 = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="0", command = lambda:btnClick("0"))
b0.grid(row=4, column=1)

b_eq = Button(root, padx=17, pady=17, bd=8, fg="black", font=('arial',20,'bold'),
                text="=", command = btnEquals)
b_eq.grid(row=4, column=2)


root.mainloop()
