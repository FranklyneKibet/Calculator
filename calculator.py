from tkinter import *
import parser
from math import factorial


root = Tk()
root.title('Calculator')

#Adding input field
display = Entry(root, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Defining functions
def get_variables():  
    return
    
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
Button(root,text='%').grid(row=1,column=4)
Button(root,text='AC').grid(row=1,column=5)
Button(root,text='÷').grid(row=2,column=5)
Button(root,text='x').grid(row=3,column=5)
Button(root,text='-').grid(row=4,column=5)
Button(root,text='+').grid(row=5,column=5)
Button(root,text='=').grid(row=5,column=4)
Button(root,text='.').grid(row=5,column=3)
Button(root,text='(').grid(row=1,column=2)
Button(root,text=')').grid(row=1,column=3)

#Adding Advanced  Operations
Button(root,text='Del').grid(row=1,column=0)
Button(root,text='ln').grid(row=1,column=1)
Button(root,text='x!').grid(row=2,column=0)
Button(root,text='sin').grid(row=2,column=1)
Button(root,text='cos').grid(row=3,column=1)
Button(root,text='tan').grid(row=4,column=1)
Button(root,text='π').grid(row=3,column=0)
Button(root,text='log').grid(row=4,column=0)
Button(root,text='Exp').grid(row=5,column=0)
Button(root,text='x^y').grid(row=5,column=1)


root.mainloop()

