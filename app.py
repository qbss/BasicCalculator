import tkinter
from tkinter import *
import math

root=Tk()
root.title("Basic Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

equation= ""

def show(value):
    global equation
    equation += str(value)
    Label_result.config(text=equation)
    equation+-value
    Label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result = eval(equation)
            # Only show decimal if needed
            if isinstance(result, float) and result.is_integer():
                result = int(result)        

        except:
            result = "Error"
            equation = ""

    Label_result.config(text=result)

def sqrt():
    global equation
    try:
        # Evaluate the current equation and take the square root
        result = math.sqrt(float(eval(equation)))
        # Only show decimal if needed
        if result.is_integer():
            result = int(result)    
        equation = str(result)
        Label_result.config(text=equation)
    except:
        Label_result.config(text="Error")
        equation = ""

def percent():
    global equation
    try:
        result = float(eval(equation)) / 100
        # Only show decimal if needed
        if result.is_integer():
            result = int(result)
        equation = str(result)
        Label_result.config(text=equation)
    except:
        Label_result.config(text="Error")
        equation = ""        

Label_result=Label(root,width=25,height=2,text="",font=("arial",30))
Label_result.pack()

Button(root, text="c", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)
Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("1")).place(x=10, y=200)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("2")).place(x=150, y=200)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("3")).place(x=290, y=200)
Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("7")).place(x=10, y=400)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("8")).place(x=150, y=400)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("9")).place(x=290, y=400)
Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("0")).place(x=10, y=500)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("+")).place(x=430, y=100)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("-")).place(x=430, y=200)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("*")).place(x=430, y=300)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("/")).place(x=430, y=400)
Button(root, text="=", width=10, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: calculate()).place(x=300, y=500)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: percent()).place(x=150, y=100)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show(".")).place(x=150, y=500)
Button(root, text="√", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: sqrt()).place(x=290, y=100)


# Button(root, text="(", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=290, y=100)
# Button(root, text=")", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=430, y=500)

# Button(root, text="x^2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=430, y=100)
# Button(root, text="x^y", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=10, y=100)
# Button(root, text="x^3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=150, y=100)
# Button(root, text="x^y", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=290, y=100)


root.mainloop()