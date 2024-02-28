from tkinter import *

class Calc:
    
    def __init__(self):

        self.window = Tk()
        self.window.title("Calc")
        self.window.resizable(0,0)

        self.screenNumbers = Entry(self.window, font="Arial 20 bold", bg="#0d1b2a", fg="white", width=24, bd=0)
        self.screenNumbers.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button1 = Button(self.frame, bg="#0d1b2a", bd=0, text="1", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("1"))
        self.button2 = Button(self.frame, bg="#0d1b2a", bd=0, text="2", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("2"))
        self.button3 = Button(self.frame, bg="#0d1b2a", bd=0, text="3", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("3"))
        self.button4 = Button(self.frame, bg="#0d1b2a", bd=0, text="4", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("4"))
        self.button5 = Button(self.frame, bg="#0d1b2a", bd=0, text="5", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("5"))
        self.button6 = Button(self.frame, bg="#0d1b2a", bd=0, text="6", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("6"))
        self.button7 = Button(self.frame, bg="#0d1b2a", bd=0, text="7", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("7"))
        self.button8 = Button(self.frame, bg="#0d1b2a", bd=0, text="8", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("8"))
        self.button9 = Button(self.frame, bg="#0d1b2a", bd=0, text="9", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("9"))
        self.button0 = Button(self.frame, bg="#0d1b2a", bd=0, text="0", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("0"))
        self.buttonIncrease = Button(self.frame, bg="#0d1b2a", bd=0, text="+", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("+"))
        self.buttonDivison = Button(self.frame, bg="#0d1b2a", bd=0, text="/", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("/"))
        self.buttonMulti = Button(self.frame, bg="#0d1b2a", bd=0, text="*", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("*"))
        self.buttonSub = Button(self.frame, bg="#0d1b2a", bd=0, text="-", font="Arial 20 bold", fg="white", width=5, height=3, command=lambda: self.touch("-"))
        self.buttonClear = Button(self.frame, bg="#0d1b2a", bd=0, text="C", font="Arial 20 bold", fg="white", width=5, height=3, command= self.Clean)
        self.buttonEqual = Button(self.frame, bg="#0d1b2a", bd=0, text="=", font="Arial 20 bold", fg="white", width=5, height=3, command= self.total)
        

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.buttonDivison.grid(row=0, column=3)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.buttonMulti.grid(row=1, column=3)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.button0.grid(row=3, column=0)
        self.buttonSub.grid(row=2, column=3)
        self.buttonIncrease.grid(row=3, column=3)
        self.buttonClear.grid(row=3, column=2)
        self.buttonEqual.grid(row=3, column=1)

        self.window.mainloop()

    def touch(self, num):
        self.screenNumbers.insert(END, num)
        
    def Clean(self):
        self.screenNumbers.delete(0, END)
        
    def total(self):
        t = eval(self.screenNumbers.get())
        self.screenNumbers.delete(0, END)
        self.screenNumbers.insert(0, str(t))
        
Calc()