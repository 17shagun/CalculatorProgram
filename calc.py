import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("Calculator")

heading_label = tk.Label(mainWindow, text='Enter first number',pady=(10),padx=(20))
heading_label.pack()
name_field = tk.Entry(mainWindow)
name_field.pack()


heading_label = tk.Label(mainWindow, text='Enter second number')
heading_label.pack()
name_field2 = tk.Entry(mainWindow)
name_field2.pack()

heading_label = tk.Label(mainWindow, text='Operation')
heading_label.pack()





button = tk.Button(mainWindow, text='Add', command=lambda: addition())
button.pack()
button = tk.Button(mainWindow, text='Subtract', command=lambda: subtraction())
button.pack()
button = tk.Button(mainWindow, text='Multiply', command=lambda: multiplication())
button.pack()
button = tk.Button(mainWindow, text='Division', command=lambda: division())
button.pack()
button = tk.Button(mainWindow, text='Modulo', command=lambda: modulo())
button.pack()
result_label=tk.Label(mainWindow,text='operation result is')
def addition():
    first=int(name_field.get())
    second=int(name_field2.get())
    result=first+second
    print("result is",result)

    result_label.config(text="operation is "+str(result))
    result_label.pack()

def subtraction():
    first = int(name_field.get())
    second = int(name_field2.get())
    result = first + second
    print("result is", result)

    result_label.config(text="operation is "+str(result))
    result_label.pack()

def multiplication():
    first = int(name_field.get())
    second = int(name_field2.get())
    result = first * second
    print("result is", result)

    result_label.config(text="operation is "+str(result))
    result_label.pack()

def division():
    first = int(name_field.get())
    second = int(name_field2.get())

    try:

            result = first / second
            print(" division result is", result)

            result_label.config(text="operation is " + str(result))

    except ZeroDivisionError:
        messagebox.showerror(ZeroDivisionError,"division by zero")

        result_label.pack()



def modulo():
    first = int(name_field.get())
    second = int(name_field2.get())
    result = first % second
    print("result is", result)

    result_label.config(text="operation is "+str(result))
    result_label.pack()
mainWindow.mainloop()