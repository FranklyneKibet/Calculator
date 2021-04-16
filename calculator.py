from tkinter import *
import parser
from math import factorial


root = Tk()
root.title('Calculator')

#Adding input field
display = Entry(root, borderwidth=5, width=90)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=15)

#Defining functions
i=0
def get_variables(num):
    global i  
    display.insert(i,num)
    i +=1   
     
#Adding Buttons 
Button(root, text='1', padx=40,pady=20,command=lambda: get_variables(1)).grid(row=4, column=2)
Button(root, text='2', padx=40,pady=20,command=lambda: get_variables(2)).grid(row=4, column=3)
Button(root, text='3', padx=40,pady=20,command=lambda: get_variables(3)).grid(row=4, column=4)
Button(root, text='4', padx=40,pady=20,command=lambda: get_variables(4)).grid(row=3, column=2)
Button(root, text='5', padx=40,pady=20,command=lambda: get_variables(5)).grid(row=3, column=3)
Button(root, text='6', padx=40,pady=20,command=lambda: get_variables(6)).grid(row=3, column=4)
Button(root, text='7', padx=40,pady=20,command=lambda: get_variables(7)).grid(row=2, column=2)
Button(root, text='8', padx=40,pady=20,command=lambda: get_variables(8)).grid(row=2, column=3)
Button(root, text='9', padx=40,pady=20,command=lambda: get_variables(9)).grid(row=2, column=4)
Button(root, text='0', padx=40,pady=20,command=lambda: get_variables(0)).grid(row=5, column=2)

#Adding operations button
Button(root,text='%', padx=38,pady=20).grid(row=1,column=4)
Button(root,text='AC', padx=35,pady=20).grid(row=1,column=5)
Button(root,text='÷', padx=38,pady=20).grid(row=2,column=5)
Button(root,text='x', padx=39,pady=20).grid(row=3,column=5)
Button(root,text='-', padx=40,pady=20).grid(row=4,column=5)
Button(root,text='+', padx=38,pady=20).grid(row=5,column=5)
Button(root,text='=', padx=39,pady=20).grid(row=5,column=4)
Button(root,text='.', padx=41,pady=20).grid(row=5,column=3)
Button(root,text='(', padx=41,pady=20).grid(row=1,column=2)
Button(root,text=')', padx=41,pady=20).grid(row=1,column=3)

#Adding Advanced  Operations
Button(root,text='Del', padx=34,pady=20).grid(row=1,column=0)
Button(root,text='ln', padx=40,pady=20).grid(row=1,column=1)
Button(root,text='x!', padx=38,pady=20).grid(row=2,column=0)
Button(root,text='sin', padx=37.4,pady=20).grid(row=2,column=1)
Button(root,text='cos', padx=35.6,pady=20).grid(row=3,column=1)
Button(root,text='tan', padx=36.4,pady=20).grid(row=4,column=1)
Button(root,text='π', padx=38,pady=20).grid(row=3,column=0)
Button(root,text='log', padx=33,pady=20).grid(row=4,column=0)
Button(root,text='Exp', padx=32,pady=20).grid(row=5,column=0)
Button(root,text='x^y', padx=34.8,pady=20).grid(row=5,column=1)

root.resizable(False,False)
root.mainloop()

