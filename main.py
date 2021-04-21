from tkinter import *

root = Tk()
root.title("Calculator")
# Entry
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=5,pady=10)

# Functions

def number(num):
	number = e.get()
	e.delete(0, END)
	e.insert(0, str(number)+str(num))

def add():
	nums = e.get()
	global num1
	global math
	num1 = float(nums)
	math = 'addition'
	e.delete(0,END)

def power():
	nums = e.get()
	global num1
	global math
	num1 = float(nums)
	math = 'power'
	e.delete(0, END)


def minus():
	nums = e.get()
	global num1
	global math
	num1 = float(nums)
	math = 'subtraction'
	e.delete(0,END)

def multiply():
	nums = e.get()
	global num1
	global math
	num1 = float(nums)
	math = 'multiplication'
	e.delete(0,END)

def divide():
	nums = e.get()
	global num1
	global math
	num1 = float(nums)
	math = 'division'
	e.delete(0,END)

def clear():
	e.delete(0, END)

def equal():
	num2 = e.get()
	e.delete(0, END)
	if math == 'addition':
		e.insert(0, num1 + float(num2))
	elif math == 'subtraction':
		e.insert(0, num1 - float(num2))
	elif math == 'multiplication':
		e.insert(0, num1 * float(num2))
	elif math == 'division':
		e.insert(0, num1 / float(num2))
	elif math == 'power':
		e.insert(0, num1 ** float(num2))
	elif math != 'addition:' or 'subtraction' or 'multiplication' or 'division' or 'power':
		e.insert(0, "None")
#Buttons

button1 = Button(root, padx= 20, pady=20, text='1', command= lambda: number(1))
button2 = Button(root, padx= 20, pady=20, text='2', command= lambda: number(2))
button3 = Button(root, padx= 20, pady=20, text='3', command= lambda: number(3))
button4 = Button(root, padx= 20, pady=20, text='4', command= lambda: number(4))
button5 = Button(root, padx= 20, pady=20, text='5', command= lambda: number(5))
button6 = Button(root, padx= 20, pady=20, text='6', command= lambda: number(6))
button7 = Button(root, padx= 20, pady=20, text='7', command= lambda: number(7))
button8 = Button(root, padx= 20, pady=20, text='8', command= lambda: number(8))
button9 = Button(root, padx= 20, pady=20, text='9', command= lambda: number(9))
button0 = Button(root, padx= 20, pady=20, text='0', command= lambda: number(0))
button00 = Button(root, padx=17, pady=20, text='00', command= lambda: number("00"))
buttonpoint = Button(root, padx= 20, pady=20, text='.', command= lambda: number("."))
negativeButton = Button(root, padx=20,pady=20, text='-', command=lambda: number("-"))

powerButton = Button(root, padx=20, pady=20,text="^",command=power)
minusButton = Button(root, padx=20, pady=20, text='_', command=minus)
plusButton = Button(root, padx=20, pady=20, text='+', command=add)
multiplyButton = Button(root, padx=20, pady=20, text='*',command=multiply)
divideButton = Button(root, padx = 20, pady = 20, text='/', command=divide)
equalButton = Button(root, padx=20, pady=20, text='=', command=equal)
clearButton = Button(root, padx=20, pady=20, text='C', command=clear)


def button():
	button1.grid(row=4, column=1)
	button2.grid(row=4, column=2)
	button3.grid(row=4, column=3)

	button4.grid(row=3, column=1)
	button5.grid(row=3, column=2)
	button6.grid(row=3, column=3)

	button7.grid(row=2, column=1)
	button8.grid(row=2, column=2)
	button9.grid(row=2, column=3)

	button00.grid(row=5, column=2)
	button0.grid(row=5, column=1)
	buttonpoint.grid(row=5, column=3)

	plusButton.grid(row=4, column=4)
	equalButton.grid(row=5, column=4)
	minusButton.grid(row=3, column=4)
	multiplyButton.grid(row=2,column=4)

	negativeButton.grid(row=1,column=1)
	powerButton.grid(row=1, column=3)
	clearButton.grid(row=1, column=2)
	divideButton.grid(row=1, column=4)
button()
mainloop()
    