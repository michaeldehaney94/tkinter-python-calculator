from tkinter import *
import parser

root = Tk()
root.title('Calculator')
# global variable used in functions
i = 0


# get user input and display data
def get_input(num):
    global i
    display.insert(i, num)
    i += 1


# calculate input
def calculate():
    entire_string = display.get()
    try:
        data = parser.expr(entire_string).compile()
        result = eval(data)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')


# clear input entire display
def clear_all():
    display.delete(0, END)


# perform arithmetic operation
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# undo or clear one value at a time
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, 'Error')


# input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# buttons
Button(root, text='1', command=lambda: get_input(1)).grid(row=2, column=0)
Button(root, text='2', command=lambda: get_input(2)).grid(row=2, column=1)
Button(root, text='3', command=lambda: get_input(3)).grid(row=2, column=2)

Button(root, text='4', command=lambda: get_input(4)).grid(row=3, column=0)
Button(root, text='5', command=lambda: get_input(5)).grid(row=3, column=1)
Button(root, text='6', command=lambda: get_input(6)).grid(row=3, column=2)

Button(root, text='7', command=lambda: get_input(7)).grid(row=4, column=0)
Button(root, text='8', command=lambda: get_input(8)).grid(row=4, column=1)
Button(root, text='9', command=lambda: get_input(9)).grid(row=4, column=2)

# arithmetic operator buttons
Button(root, text='AC', command=clear_all).grid(row=5, column=0)
Button(root, text='0', command=lambda: get_input(0)).grid(row=5, column=1)
Button(root, text='=', command=lambda: calculate()).grid(row=5, column=2)

Button(root, text='+', command=lambda: get_operation('+')).grid(row=2, column=3)
Button(root, text='-', command=lambda: get_operation('-')).grid(row=3, column=3)
Button(root, text='*', command=lambda: get_operation('*')).grid(row=4, column=3)
Button(root, text='/', command=lambda: get_operation('/')).grid(row=5, column=3)

# more arithmetic operator button
Button(root, text='π', command=lambda: get_operation('* 3.14')).grid(row=2, column=4)
Button(root, text='%', command=lambda: get_operation('%')).grid(row=3, column=4)
Button(root, text='(', command=lambda: get_operation('(')).grid(row=4, column=4)
Button(root, text='exp', command=lambda: get_operation('**')).grid(row=5, column=4)

Button(root, text='<-', command=lambda: undo()).grid(row=2, column=5)
Button(root, text='x!', command=lambda: get_operation('x!')).grid(row=3, column=5)
Button(root, text=')', command=lambda: get_operation(')')).grid(row=4, column=5)
Button(root, text='^2', command=lambda: get_operation('**2')).grid(row=5, column=5)

root.mainloop()
