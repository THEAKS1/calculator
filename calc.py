from tkinter import *
from tkinter.messagebox import *
import math

class Calculator:

    def equ(self):
        self.expression = self.display.get("1.0",END)
        self.display.delete(1.0, END)
        try:
            self.output = eval(self.expression)
            self.display.insert(END, str(self.output))
        except:
            try:
                self.output = math.factorial(int(self.expression[:-2]))
                self.display.insert(END, str(self.output))
            except:
                showerror("ERROR", "Invalid expression!")

    def erase(self):
        self.expression = self.display.get(1.0,END)
        self.display.delete(1.0, END)
        self.display.insert(END, self.expression[:-2])

    def window(self):
        self.flip = True
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("400x500")

        self.buttons1()
     
        self.display = Text(height = 5, width = 26, font = ("Arial", 20))
        self.display.pack()

        self.win.mainloop()

    def buttons1(self):

        self.clear = Button(self.win, text = "C", fg = "Red", height = 1, width = 5, command = lambda : self.display.delete(1.0,END), font = ("Arial", 20))
        self.clear.place(x = 4, y = 170)

        self.backspace = Button(self.win, text = "<-", fg = "Red", height = 1, width = 5, command = self.erase, font = ("Arial", 20))
        self.backspace.place(x = 105, y = 170)

        self.percent = Button(self.win, text = "%", fg = "Red", height = 1, width = 5, command = lambda : self.display.insert(END, "%"), font = ("Arial", 20))
        self.percent.place(x = 205, y = 170)

        self.divide = Button(self.win, text = "/", fg = "Red", height = 1, width = 5, command = lambda : self.display.insert(END, "/"), font = ("Arial", 20))
        self.divide.place(x = 305, y = 170)

        self.mul = Button(self.win, text = "X", fg = "Red", height = 1, width = 5, command = lambda : self.display.insert(END, "*"), font = ("Arial", 20))
        self.mul.place(x = 305, y = 235)

        self.minus = Button(self.win, text = "-", fg = "Red", height = 1, width = 5, command = lambda : self.display.insert(END, "-"), font = ("Arial", 20))
        self.minus.place(x = 305, y = 300)

        self.plus = Button(self.win, text = "+", fg = "Red", height = 1, width = 5, command = lambda : self.display.insert(END, "+"), font = ("Arial", 20))
        self.plus.place(x = 305, y = 365)

        self.equals = Button(self.win, text = "=", fg = "Red", height = 1, width = 5, command = self.equ, font = ("Arial", 20))
        self.equals.place(x = 305, y = 430)

        self.nine = Button(self.win, text = "9", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "9"), font = ("Arial", 20))
        self.nine.place(x = 205, y = 235)

        self.six = Button(text = "6", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "6"), font = ("Arial", 20))
        self.six.place(x = 205, y = 300)

        self.three = Button(self.win, text = "3", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "3"), font = ("Arial", 20))
        self.three.place(x = 205, y = 365)

        self.decimal = Button(self.win, text = ".", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "."), font = ("Arial", 20))
        self.decimal.place(x = 205, y = 430)

        self.eight = Button(self.win, text = "8", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "8"), font = ("Arial", 20))
        self.eight.place(x = 105, y = 235)

        self.five = Button(self.win, text = "5", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "5"), font = ("Arial", 20))
        self.five.place(x = 105, y = 300)

        self.two = Button(self.win, text = "2", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "2"), font = ("Arial", 20))
        self.two.place(x = 105, y = 365)

        self.zero = Button(self.win, text = "0", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "0"), font = ("Arial", 20))
        self.zero.place(x = 105, y =430)

        self.seven = Button(self.win, text = "7", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "7"), font = ("Arial", 20))
        self.seven.place(x = 4, y = 235)

        self.four = Button(self.win, text = "4", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "4"), font = ("Arial", 20))
        self.four.place(x = 4, y = 300)

        self.one = Button(self.win, text = "1", fg = "black", height = 1, width = 5, command = lambda : self.display.insert(END, "1"), font = ("Arial", 20))
        self.one.place(x = 4, y = 365)

        self.more = Button(self.win, text = "More", fg = "black", height = 1, width = 5, command = self.flip_keys, font = ("Arial", 20))
        self.more.place(x = 4, y = 430)

        self.flip = True

    def flip_keys(self):
        self.clear.destroy()
        self.backspace.destroy()
        self.percent.destroy()
        self.divide.destroy()
        self.mul.destroy()
        self.more.destroy()
        self.minus.destroy()
        self.plus.destroy()
        self.equals.destroy()
        self.one.destroy()
        self.two.destroy()
        self.three.destroy()
        self.four.destroy()
        self.five.destroy()
        self.six.destroy()
        self.seven.destroy()
        self.eight.destroy()
        self.nine.destroy()
        self.zero.destroy()
        self.decimal.destroy()
        if self.flip:
            self.buttons2()
        else:
            self.buttons1()


    def buttons2(self):

        self.clear = Button(self.win, text = "C", fg = "Red", height = 1, width = 3, command = lambda : self.display.delete(1.0,END), font = ("Arial", 20))
        self.clear.place(x = 85, y = 170)

        self.backspace = Button(self.win, text = "<-", fg = "Red", height = 1, width = 3, command = self.erase, font = ("Arial", 20))
        self.backspace.place(x = 165, y = 170)

        self.percent = Button(self.win, text = "%", fg = "Red", height = 1, width = 3, command = lambda : self.display.insert(END, "%"), font = ("Arial", 20))
        self.percent.place(x = 245, y = 170)

        self.divide = Button(self.win, text = "/", fg = "Red", height = 1, width = 3, command = lambda : self.display.insert(END, "/"), font = ("Arial", 20))
        self.divide.place(x = 325, y = 170)

        self.mul = Button(self.win, text = "X", fg = "Red", height = 1, width = 3, command = lambda : self.display.insert(END, "*"), font = ("Arial", 20))
        self.mul.place(x = 325, y = 235)

        self.minus = Button(self.win, text = "-", fg = "Red", height = 1, width = 3, command = lambda : self.display.insert(END, "-"), font = ("Arial", 20))
        self.minus.place(x = 325, y = 300)

        self.plus = Button(self.win, text = "+", fg = "Red", height = 1, width = 3, command = lambda : self.display.insert(END, "+"), font = ("Arial", 20))
        self.plus.place(x = 325, y = 365)

        self.equals = Button(self.win, text = "=", fg = "Red", height = 1, width = 3, command = self.equ, font = ("Arial", 20))
        self.equals.place(x = 325, y = 430)

        self.nine = Button(self.win, text = "9", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "9"), font = ("Arial", 20))
        self.nine.place(x = 245, y = 235)

        self.six = Button(text = "6", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "6"), font = ("Arial", 20))
        self.six.place(x = 245, y = 300)

        self.three = Button(self.win, text = "3", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "3"), font = ("Arial", 20))
        self.three.place(x = 245, y = 365)

        self.decimal = Button(self.win, text = ".", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "."), font = ("Arial", 20))
        self.decimal.place(x = 245, y = 430)

        self.eight = Button(self.win, text = "8", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "8"), font = ("Arial", 20))
        self.eight.place(x = 165, y = 235)

        self.five = Button(self.win, text = "5", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "5"), font = ("Arial", 20))
        self.five.place(x = 165, y = 300)

        self.two = Button(self.win, text = "2", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "2"), font = ("Arial", 20))
        self.two.place(x = 165, y = 365)

        self.zero = Button(self.win, text = "0", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "0"), font = ("Arial", 20))
        self.zero.place(x = 165, y =430)

        self.seven = Button(self.win, text = "7", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "7"), font = ("Arial", 20))
        self.seven.place(x = 85, y = 235)

        self.four = Button(self.win, text = "4", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "4"), font = ("Arial", 20))
        self.four.place(x = 85, y = 300)

        self.one = Button(self.win, text = "1", fg = "black", height = 1, width = 3, command = lambda : self.display.insert(END, "1"), font = ("Arial", 20))
        self.one.place(x = 85, y = 365)

        self.more = Button(self.win, text = "Less", fg = "black", height = 1, width = 3, command = self.flip_keys, font = ("Arial", 20))
        self.more.place(x = 85, y = 430)

        self.openb = Button(self.win, text = "(", fg = "blue", height = 1, width = 3, command = lambda : self.display.insert(END, "("), font = ("Arial", 20))
        self.openb.place(x = 5, y = 170)

        self.closeb = Button(self.win, text = ")", fg = "blue", height = 1, width = 3, command = lambda : self.display.insert(END, ")"), font = ("Arial", 20))
        self.closeb.place(x = 5, y = 235)

        self.pi = Button(self.win, text = "pi", fg = "blue", height = 1, width = 3, command = lambda : self.display.insert(END, "3.14"), font = ("Arial", 20))
        self.pi.place(x = 5, y = 300)

        self.reciprocal = Button(self.win, text = "1/x", fg = "blue", height = 1, width = 3, command = lambda : self.display.insert(END, "1/"), font = ("Arial", 20))
        self.reciprocal.place(x = 5, y = 365)

        self.factorial = Button(self.win, text = "x!", fg = "blue", height = 1, width = 3, command = lambda : self.display.insert(END, "!"), font = ("Arial", 20))
        self.factorial.place(x = 5, y = 430)

        self.flip = False

cal = Calculator()
cal.window()