from tkinter import *
from ttkthemes import ThemedTk
from tkinter import ttk
import random
window = ThemedTk(theme="black")
window.configure(themebg ="black")
window.title("Calculator")

var=StringVar()
result = ""
def clear():
    global result
    result = ""
    var = ""
def press(num):
    global result
    result = result + str(num)
    var.set(result)
def equalpress():
    try:
        global result
        total= str(eval(result))
        var.set(total)
        result=""

    except:
        var.set(' Error ')
        result = ""

def backspace():
    global result
    result = txt.get()[:-1]
    if result == "":
        result = ""
    var.set(result)

btn1 =ttk.Button(window,text="1", command=lambda : press(1))
btn1.grid(column=0,row=1,)
btn2 =ttk.Button(window,text="2", command=lambda : press(2))
btn2.grid(column=2,row=1)
btn3 =ttk.Button(window,text="3", command=lambda : press(3))
btn3.grid(column=3,row=1)
btn4 =ttk.Button(window,text="4", command=lambda : press(4))
btn4.grid(column=0,row=2)
btn5 =ttk.Button(window,text="5", command=lambda : press(5))
btn5.grid(column=2,row=2)
btn6 =ttk.Button(window,text="6", command=lambda : press(6))
btn6.grid(column=3,row=2)

btn7 =ttk.Button(window,text="7", command=lambda : press(7))
btn7.grid(column=0,row=3)
btn8 =ttk.Button(window,text="8", command=lambda : press(8))
btn8.grid(column=2,row=3)
btn9 =ttk.Button(window,text="9", command=lambda : press(9))
btn9.grid(column=3,row=3)

btn0 =ttk.Button(window,text="0", command=lambda : press(0))
btn0.grid(column=0,row=4)
btn00 =ttk.Button(window,text="=", command = equalpress)
btn00.grid(column=3,row=4)
btnC =ttk.Button(window,text="Clear",command = clear)
btnC.grid(column=2,row=4)

btnp =ttk.Button(window,text="+", command=lambda : press('+'))
btnp.grid(column=4,row=1)
btnm =ttk.Button(window,text="-", command=lambda : press('-'))
btnm.grid(column=4,row=2)
btnX =ttk.Button(window,text="x", command=lambda : press('*'))
btnX.grid(column=4,row=3)
btnL =ttk.Button(window,text="/", command=lambda : press('/'))
btnL.grid(column=4,row=4)

btnQ =ttk.Button(window,text="pi", command=lambda : press(3.14))
btnQ.place(x=100, y= 125)
btnQ2 =ttk.Button(window,text=".", command=lambda : press("."))
btnQ2.place(x=25, y= 125)
btnPOWER =ttk.Button(window,text="POWER", command=lambda : press("**"))
btnPOWER.place(x=25, y= 150)

btnRANDOM =ttk.Button(window,text="RANDOM", command=lambda : press(random.randint(1,100)))
btnRANDOM.place(x=100, y= 150)

btnRANDOM2 =ttk.Button(window,text="SRandom", command=lambda : press(random.randint(189,999999)))
btnRANDOM2.place(x=25, y= 200)

btnPRD =ttk.Button(window,text="(", command=lambda : press ('(') )
btnPRD.place(x=25, y= 225)
btnPRD =ttk.Button(window,text=")", command=lambda : press (')') )
btnPRD.place(x=100, y= 225)

btnBACK =ttk.Button(window,text="Back", command=backspace)
btnBACK.place(x=25, y= 175)


txt = Entry(window,width=42, text=var)
txt.grid(column=0, row=0, columnspan= 5)



window.geometry('250x250')
window.mainloop()