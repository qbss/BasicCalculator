import tkinter
from tkinter import *

root=TK()
root.title("Basic Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="black")

Label_result=Label(root,text="Result",bg="black",fg="white",font=("Arial",20))

root.mainloop()