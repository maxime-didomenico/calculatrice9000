from tkinter import *
import csv

string = ""

calc = Tk()

def button_click(num):
    global string
    string = string + str(num)
    expr.set(string)

def ft_result():
    global string
    result = str(eval(string)) 
    expr.set(result)
    with open('history.csv', 'a', newline='') as csvfile:
        fieldnames = ['expression', 'res']

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()
        thewriter.writerow({'expression' : string, 'res' : result})

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
calc.geometry("525x390")
calc.resizable(width=False, height=False)

expr=StringVar()

display = Entry(calc, width = 54, bd = 2, justify = 'right', textvariable=expr, state=DISABLED, disabledbackground='white', disabledforeground='black')
display.grid(columnspan = 4, pady= 20 , padx =10 , ipadx = 5 , ipady = 10)

pi = Button(calc, bg='grey', text="π", height=2, width= 10, command=lambda : button_click("3.1415"))
pi.grid(row = 1, column = 0)

fact = Button(calc, text="x!", bg='grey',  height=2, width= 10, command=lambda : ft_factorial(int(string)))
fact.grid(row = 1, column = 1)
    
# = Button(calc, text="x²", height=2, width= 10, command=lambda : ft_pow(int(string)))
#.grid(row = 1, column = 2)

# = Button(calc, text="*", height=2, width=10, command=lambda: button_click("*"))
#.grid(row = 1, column = 3)

sqrt = Button(calc, text="√", bg='grey', height=2, width= 10, command=lambda : ft_sqrt(int(string)))
sqrt.grid(row = 2, column = 0)

percent = Button(calc, text="%", bg='grey',  height=2, width= 10, command=lambda : button_click("%"))
percent.grid(row = 2, column = 1)
    
pow = Button(calc, text="x²", bg='grey', height=2, width= 10, command=lambda : ft_pow(int(string)))
pow.grid(row = 2, column = 2)

multiply = Button(calc, text="*", bg='grey', height=2, width=10, command=lambda : button_click("*"))
multiply.grid(row = 2, column = 3)


one = Button(calc, text="1", height=2, bg='white', width= 10, command=lambda : button_click("1"))
one.grid(row = 3, column = 0)

two = Button(calc, text="2", bg='white',  height=2, width= 10, command=lambda : button_click("2"))
two.grid(row = 3, column = 1)
    
three = Button(calc, text="3", bg='white', height=2, width= 10, command=lambda : button_click("3"))
three.grid(row = 3, column = 2)

plus = Button(calc, text="+", bg='grey', height=2, width=10, command=lambda : button_click("+"))
plus.grid(row = 3, column = 3)
    


four = Button(calc, text="4", bg='white', height=2, width=10, command=lambda : button_click("4"))
four.grid(row = 4, column = 0)

five = Button(calc, text="5", bg='white', height=2, width=10, command=lambda : button_click("5"))
five.grid(row = 4, column = 1)
    
six = Button(calc, text="6", bg='white', height=2, width=10, command=lambda : button_click("6"))
six.grid(row = 4, column = 2)

minus = Button(calc, text="-", bg='grey', height=2, width=10, command=lambda : button_click("-"))
minus.grid(row = 4, column = 3)
    


seven = Button(calc, text="7", bg='white', height=2, width=10, command=lambda : button_click("7"))
seven.grid(row = 5, column = 0)

eight = Button(calc, text="8", bg='white' , height=2, width=10, command=lambda : button_click("8"))
eight.grid(row = 5, column = 1)
    
nine = Button(calc, text="9", bg='white' , height=2, width=10, command=lambda : button_click("9"))
nine.grid(row = 5, column = 2)

divide = Button(calc, text="/", bg='grey', height=2, width=10, command=lambda : button_click("/"))
divide.grid(row = 5, column = 3)
   


zero = Button(calc, text="0", bg='white', height=2, width=10, command=lambda : button_click("0"))
zero.grid(row = 6, column = 0)
   
coma = Button(calc, text=",", bg='grey', height=2, width=10, command=lambda : button_click("."))
coma.grid(row = 6, column = 1)

erase = Button(calc, text="AC", bg='grey', height=2, width=10, command=lambda : ft_erase())
erase.grid(row = 6, column = 2)

equal = Button(calc, bg='orange', text="=", height=2, width=10, command=lambda : ft_result())
equal.grid(row = 6, column = 3)

calc.mainloop()