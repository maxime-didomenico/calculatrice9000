from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv

string = ""

calc = tk.Tk()

def button_click(num):
    global string
    string = string + str(num)
    expr.set(string)

def ft_result():
    global string
    result = str(eval(string)) 
    expr.set(result)
    string2 = StringVar()
    string3 = str(string + "="  + str(result))
    string2.set(string3)
    ps = Label(history,textvariable=string2,pady=20, text="test")
    ps.pack()

def ft_erase():
    global string
    string = ""
    expr.set("")

def ft_sqrt(n):
    if n < 0:
        expr.set("error")
    else:
        result =  n ** 0.5
        expr.set(result)

def ft_factorial(n):
    result = 1
    i = 0
    while i < n:
        result = result*(i+1)
        i+=1
    expr.set(result)


def ft_pow(n):
    result =  n ** 2
    expr.set(result)

    
calc.title("Calculatrice over 9000")
calc.geometry("525x410")
calc.resizable(width=False, height=False)

expr=StringVar()

tabControl = ttk.Notebook(calc)

calculator = ttk.Frame(tabControl)
history = ttk.Frame(tabControl)

tabControl.add(calculator, text ='Calculator')
tabControl.add(history, text ='History')
tabControl.pack(expand = 1, fill ="both")

display = Entry(calculator, width = 54, bd = 2, justify = 'right', textvariable=expr, state=DISABLED, disabledbackground='white', disabledforeground='black')
display.grid(columnspan = 4, pady= 20 , padx =10 , ipadx = 5 , ipady = 10)

pi = Button(calculator, bg='grey', text="π", height=2, width= 10, command=lambda : button_click("3.1415"))
pi.grid(row = 1, column = 0)

fact = Button(calculator, text="x!", bg='grey',  height=2, width= 10, command=lambda : ft_factorial(int(string)))
fact.grid(row = 1, column = 1)
    
# = Button(calc, text="x²", height=2, width= 10, command=lambda : ft_pow(int(string)))
#.grid(row = 1, column = 2)

# = Button(calc, text="*", height=2, width=10, command=lambda: button_click("*"))
#.grid(row = 1, column = 3)

sqrt = Button(calculator, text="√", bg='grey', height=2, width= 10, command=lambda : ft_sqrt(int(string)))
sqrt.grid(row = 2, column = 0)

percent = Button(calculator, text="%", bg='grey',  height=2, width= 10, command=lambda : button_click("%"))
percent.grid(row = 2, column = 1)
    
pow = Button(calculator, text="x²", bg='grey', height=2, width= 10, command=lambda : ft_pow(int(string)))
pow.grid(row = 2, column = 2)

multiply = Button(calculator, text="*", bg='grey', height=2, width=10, command=lambda : button_click("*"))
multiply.grid(row = 2, column = 3)


one = Button(calculator, text="1", height=2, bg='white', width= 10, command=lambda : button_click("1"))
one.grid(row = 3, column = 0)

two = Button(calculator, text="2", bg='white',  height=2, width= 10, command=lambda : button_click("2"))
two.grid(row = 3, column = 1)
    
three = Button(calculator, text="3", bg='white', height=2, width= 10, command=lambda : button_click("3"))
three.grid(row = 3, column = 2)

plus = Button(calculator, text="+", bg='grey', height=2, width=10, command=lambda : button_click("+"))
plus.grid(row = 3, column = 3)
    


four = Button(calculator, text="4", bg='white', height=2, width=10, command=lambda : button_click("4"))
four.grid(row = 4, column = 0)

five = Button(calculator, text="5", bg='white', height=2, width=10, command=lambda : button_click("5"))
five.grid(row = 4, column = 1)
    
six = Button(calculator, text="6", bg='white', height=2, width=10, command=lambda : button_click("6"))
six.grid(row = 4, column = 2)

minus = Button(calculator, text="-", bg='grey', height=2, width=10, command=lambda : button_click("-"))
minus.grid(row = 4, column = 3)
    


seven = Button(calculator, text="7", bg='white', height=2, width=10, command=lambda : button_click("7"))
seven.grid(row = 5, column = 0)

eight = Button(calculator, text="8", bg='white' , height=2, width=10, command=lambda : button_click("8"))
eight.grid(row = 5, column = 1)
    
nine = Button(calculator, text="9", bg='white' , height=2, width=10, command=lambda : button_click("9"))
nine.grid(row = 5, column = 2)

divide = Button(calculator, text="/", bg='grey', height=2, width=10, command=lambda : button_click("/"))
divide.grid(row = 5, column = 3)
   


zero = Button(calculator, text="0", bg='white', height=2, width=10, command=lambda : button_click("0"))
zero.grid(row = 6, column = 0)
   
coma = Button(calculator, text=",", bg='grey', height=2, width=10, command=lambda : button_click("."))
coma.grid(row = 6, column = 1)

erase = Button(calculator, text="AC", bg='grey', height=2, width=10, command=lambda : ft_erase())
erase.grid(row = 6, column = 2)

equal = Button(calculator, bg='orange', text="=", height=2, width=10, command=lambda : ft_result())
equal.grid(row = 6, column = 3)

calc.mainloop()