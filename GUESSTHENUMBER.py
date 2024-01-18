
from tkinter import *


import random
import time
window = Tk()
window.title("Guess the number!")

number = 0


cng = 0
#cng = CorrectNumberGuessed
tries = 0
window.geometry('300x350')
hard = 2
print(hard)

uparrow = PhotoImage(file="uparrow.png")
downarrow = PhotoImage(file="downarrow.png")
correct = PhotoImage(file="correct.png")
dice = PhotoImage(file="die.png")
tbl = Label(window , text="Guess the Number!",background="white", foreground="black", font=('Helvetica', 15, 'bold'), justify=CENTER, borderwidth=5, relief="groove")
tbl.place(x=50,y=0)
window.configure(bg="light gray")
def Randomize():
    global number
    global hard
    pic.configure(image =dice)

    cng = 0
    hard = rb.get()
    import random
    if hard == "1":
        number = random.randint(0,25)

    if hard == "2":
        number = random.randint(0,100)

    if hard == "3":
        number = random.randint(0,150)


    print(number)


def maingame(event):
    global tries
    print("maingame")
    if int(txt.get().lower()) == number:
        print("Correct!")
        tries = 0
        labl.configure(text="Tries : " + str(tries))
        cng = 1
        pic.configure(image=correct)
        txt.delete(0, 'end')


    if number > int(txt.get().lower()):
        print("Too small!")
        tries = tries + 1
        labl.configure(text="Tries : " + str(tries))
        cng = 0
        pic.configure(image= uparrow)


    if int(txt.get().lower()) > number:
        print("Too big!")
        tries = tries +1
        labl.configure(text = "Tries : " + str(tries))
        cng = 0
        pic.configure(image= downarrow)






def Exit():
    print("Player left the game. :(")
    window.destroy()


rb = StringVar()


rad1 = Radiobutton(window, text="Easy (0-25)", value="1", variable=rb)
rad1.place(x=20, y = 100)

rad2 = Radiobutton(window, text="Normal (0-100", value="2", variable=rb)
rad2.place(x=100, y = 100)

rad3 = Radiobutton(window, text="Hard (0-150)", value="3", variable=rb)
rad3.place(x=200, y = 100)

btn = Button(window, text="Randomize!", command=Randomize)

btn.place(x=200, y=250)

uparrow = PhotoImage(file="uparrow.png")

downarrow = PhotoImage(file="downarrow.png")

correct = PhotoImage(file="correct.png")

dice = PhotoImage(file="die.png")
pic= Label(window, image=dice)
pic.place(x=10, y=200)

lebl= Label(window, text="Select A difficulty before clicking randomize!")
lebl.place(x=-5,y=50)

txt = Entry(window,width=10)
txt.txt = Entry(window,width=20)
txt.place(x= 200, y= 225)

labl= Label(window, text="Tries: 0" )
labl.place(x=200,y=200)
exit = Button(window, text="Exit", command=Exit)





window.bind('<Return>', maingame)
window.mainloop()