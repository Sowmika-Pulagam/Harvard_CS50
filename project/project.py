import tkinter as tk
from tkinter import *

#Creating an empty string
calculator = ""

def main():
    addition()
    evaluation_fun()
    clear()

def addition(symbol):
    #Global variable calculator
    global calculator
    calculator += str(symbol)
    area.delete("1.0","end")
    area.insert("1.0", calculator)

def evaluation_fun():
    #Global variable calculator
    global calculator
    calculator = str(eval(calculator))
    area.delete("1.0","end")
    area.insert("1.0", calculator)

def clear():
    #Global variable calculator
    global calculator
    calculator = ""
    area.delete("1.0","end")

#For creating a calculator(GUI) window
calculator_window = Tk()
#I am specifying my window size as 300,300
calculator_window.geometry("275x275")
calculator_window.title("Calculator")
area = Text(calculator_window, height= 2, width = 16, font = ("Calibri",24))
area.grid(columnspan = 5)

#For displaying the buttons from 0 to 9(NUMBERS)
#Row 6
button0 = Button(calculator_window, text="0", command=lambda: addition(0), width=5, font=("Times New Roman",14))
button0.grid(row=6, column=2)

button_equal = Button(calculator_window, text="=", bg='Light Blue', command=lambda: evaluation_fun(), width=5, font=("Times New Roman",14))
button_equal.grid(row=6, column=4)

button_open_parenthesis = Button(calculator_window, text = "(", command=lambda: addition("("), width=5, font=("Times New Roman",14))
button_open_parenthesis.grid(row=6,column=1)

button_close_parenthesis = Button(calculator_window, text = ")", command=lambda: addition(")"), width=5, font=("Times New Roman",14))
button_close_parenthesis.grid(row=6,column=3)

#Row 5
button1 = Button(calculator_window, text="1", command=lambda: addition(1), width=5, font=("Times New Roman",14))
button1.grid(row=5, column=1)
button2 = Button(calculator_window, text="2",  command=lambda: addition(2), width=5, font=("Times New Roman",14))
button2.grid(row=5, column=2)
button3 = Button(calculator_window, text="3", command=lambda: addition(3), width=5, font=("Times New Roman",14))
button3.grid(row=5, column=3)

button_plus = Button(calculator_window, text="+", command=lambda: addition("+"), width=5, font=("Times New Roman",14))
button_plus.grid(row=5, column=4)

#Row 4
button4 = Button(calculator_window, text="4", command=lambda: addition(4), width=5, font=("Times New Roman",14))
button4.grid(row=4, column=1)
button5 = Button(calculator_window, text="5", command=lambda: addition(5), width=5, font=("Times New Roman",14))
button5.grid(row=4, column=2)
button6 = Button(calculator_window, text="6", command=lambda: addition(6),  width=5, font=("Times New Roman",14))
button6.grid(row=4, column=3)

button_minus = Button(calculator_window, text="-", command=lambda: addition("-"), width=5, font=("Times New Roman",14))
button_minus.grid(row=4, column=4)

#Row 3
button7 = Button(calculator_window, text="7", command=lambda: addition(7),  width=5, font=("Times New Roman",14))
button7.grid(row=3, column=1)
button8 = Button(calculator_window, text="8", command=lambda: addition(8), width=5, font=("Times New Roman",14))
button8.grid(row=3, column=2)
button9 = Button(calculator_window, text="9", command=lambda: addition(9),  width=5, font=("Times New Roman",14))
button9.grid(row=3, column=3)

button_multiplication = Button(calculator_window, text="*", command=lambda: addition("*"), width=5, font=("Times New Roman",14))
button_multiplication.grid(row=3, column=4)

#Row 2
button_division = Button(calculator_window, text="/", command=lambda: addition("/"), width=5, font=("Times New Roman",14))
button_division.grid(row=2, column=4)

button_decimal = Button(calculator_window, text=".", command=lambda: addition("."), width=5, font=("Times New Roman",14))
button_decimal.grid(row=2, column=3)

button_percentile = Button(calculator_window, text="%", command=lambda: addition("%"), width=5, font=("Times New Roman",14))
button_percentile.grid(row=2, column=2)

button_clear = Button(calculator_window, text="clear", command=lambda: clear(), width=5, font=("Times New Roman",14))
button_clear.grid(row=2, column=1)

calculator_window.mainloop()

if __name__ == "__main__":
    main()

