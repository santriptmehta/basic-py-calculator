import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_plus_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_multi_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def c_pressed():
    global A
    global operator
    global val

    val = ""
    A = 0
    operator = ""
    data.set(val)


def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
       X = int((val2.split("+")[1]))
       C = A + X
       data.set(C)
       val = str(C)
    elif operator == "-":
       X = int((val2.split("-")[1]))
       C = A - X
       data.set(C)
       val = str(C)
    elif operator == "*":
       X = int((val2.split("*")[1]))
       C = A*X
       data.set(C)
       val = str(C)
    elif operator == "/":
        X = int((val2.split("/")[1]))
        if X == 0:
            messagebox.showerror("Error","Division by 0 Not supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / X)
            data.set(C)
            val = str(C)

 


     
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")


data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font  = ("vardana",20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
    )
lbl.pack(expand = True, fill = "both")

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand = True, fill = "both",)
 
btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


btn1 = Button(
    btnrow1,
    text =  "1",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
    )
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text =  "2",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
    )
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text =  "3",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
    )
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow1,
    text =  "+",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked,
    
    )
btn4.pack(side = LEFT, expand = True, fill = "both",)



btn1 = Button(
    btnrow2,
    text =  "4",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
    )

btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow2,
    text =  "5",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
    )
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow2,
    text =  "6",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
    )
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow2,
    text =  "-",
    font = ("verdana", 24),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked,
    )
btn4.pack(side = LEFT, expand = True, fill = "both",)




btn1 = Button(
    btnrow3,
    text =  "7",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
    )
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(





    btnrow3,
    text =  "8",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_8_isclicked,
    )
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow3,
    text =  "9",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
    )
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow3,
    text =  "x",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_multi_clicked,
    )
btn4.pack(side = LEFT, expand = True, fill = "both",)





btn1 = Button(
    btnrow4,
    text =  "C",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = c_pressed,
    )
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow4,
    text =  "0",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow4,
    text =  "=",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow4,
    text =  "/",
    font = ("verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,
    )
btn4.pack(side = LEFT, expand = True, fill = "both",)










root.mainloop()



