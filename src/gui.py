##
# @author Otakar Sedlák (xsedla1r)
# @file gui.py
# @date 08.04.2020
#

from tkinter import *
from functools import partial
import math
import mathlib as m


## Creating window for calculator
main=Tk()
main.title("Calculator")
main.configure(bg="white")
main.resizable(width=False, height=False)

##Global variable for operation 
oper=False   
##Global variable for first number sign 
Asign=1 
##Global variable for second number sign      
Bsign=1      

##
# @brief Writing symbol on the display
# @details Written symbol depends on pressing certain button 
# @param Symbol whats going to be written
#
def Write(symbol):
    global oper
    display.insert(END, symbol)
    if symbol in "+-*/^√":
        oper=True
   
##
# @brief Deleting display, result and global variables
#
def Clear():
    global oper
    global Asign
    global Bsign
    display.delete(0,END)
    answer["text"]=""
    oper=False
    Asign=1
    Bsign=1

##
# @brief Setting variables Asign and Bsign
# @details Settings depends on positivity or negativity of the operand
#
def Sign():
    global Asign
    global Bsign
    if oper:
        Bsign=-1
    else:
        Asign=-1
    display.insert(END, "-")
   
##
# @brief Printing result on the display
# @details Using mahtlib to calculate result and then printing it
#
def Print():
    global Asign
    global Bsign
    global oper
    if oper==False:
        answer["text"]=display.get()
    text=str(display.get())
    if Asign==-1:
        text=text[1:]
    if Bsign==-1:
        text=text[len(text)::-1]        
        for i in range (0,len(text)-1):
            if text[i]=="-":
                text=text[:i]+text[i+1:]
                break
        text=text[len(text)::-1]        
    for i in range (0,len(text)-1):
        if text[i] in "+-*/^√":
            operation=text[i]
            A=text[:i]
            B=text[i+1:]
            break
    try:
        A=float(A)*Asign
        B=float(B)*Bsign
    except ValueError:
        answer["text"]="Unsupported format!"
    
    if operation=="+":
        x=m.add(A,B)
    elif operation=="-":
        x=m.sub(A,B)
    elif operation=="*":
        x=m.mul(A,B)
    elif operation=="/":
        x=m.div(A,B)
    elif operation=="^":
        x=m.pow(A,B)
    else:
        x=m.sqrr(B,A)

    if x=="error":
        answer["text"]="Math error!"
    else:
        answer["text"]=round(x,9)                  

##
# @brief Designing buttons of calculator and adding functionality
# @details Using functions from tkinter
def Components():
    global display
    global answer

    display=Entry(main, font=("Calibri",15), bg="lightblue")
    display.grid(row=0, column=0, padx=5, pady=5, columnspan=5)
    
    lEqual=Label(main, text="=", bg="white")
    lEqual.grid(row=1, column=0, padx=5, pady=5)
    answer=Label(main, text="", bg="white")
    answer.grid(row=1, column=1, padx=5, pady=5, columnspan=4)
    
    bPi=Button(main, text="π", relief="flat", bg="lightblue", command=partial(Write, str(math.pi)))
    bPi.grid(row=2, column=0, padx=5, pady=5,sticky=W+E+N+S, ipadx=6)
    bEuler=Button(main, text="e", relief="flat", bg="lightblue", command=partial(Write, str(math.e)))
    bEuler.grid(row=2, column=1, padx=5, pady=5,sticky=W+E+N+S, ipadx=6)
    bClear=Button(main, text="ϕ", relief="flat", bg="lightblue", command=partial(Write, "1.618033988749894"))
    bClear.grid(row=2, column=2, padx=5, pady=5,sticky=W+E+N+S)
    bDelete=Button(main, text="C", relief="flat", bg="#ee5555", fg="white", command=Clear)
    bDelete.grid(row=2, column=3, columnspan=2, padx=5, pady=5,sticky=W+E+N+S)
    
    b7=Button(main, text="7", relief="flat", bg="lightblue", command=partial(Write, "7"))
    b7.grid(row=3, column=0, padx=5, pady=5,sticky=W+E+N+S)
    b8=Button(main, text="8", relief="flat", bg="lightblue", command=partial(Write, "8"))
    b8.grid(row=3, column=1, padx=5, pady=5,sticky=W+E+N+S)
    b9=Button(main, text="9", relief="flat", bg="lightblue", command=partial(Write, "9"))
    b9.grid(row=3, column=2, padx=5, pady=5,sticky=W+E+N+S, ipadx=6)
    bPlus=Button(main, text="+", relief="flat", bg="#bbeeff", command=partial(Write, "+"))
    bPlus.grid(row=3, column=3, padx=5, pady=5,sticky=W+E+N+S)
    bMinus=Button(main, text="-", relief="flat", bg="#bbeeff", command=partial(Write, "-"))
    bMinus.grid(row=3, column=4, padx=5, pady=5,sticky=W+E+N+S)
    
    b4=Button(main, text="4", relief="flat", bg="lightblue", command=partial(Write, "4"))
    b4.grid(row=4, column=0, padx=5, pady=5,sticky=W+E+N+S)
    b5=Button(main, text="5", relief="flat", bg="lightblue", command=partial(Write, "5"))
    b5.grid(row=4, column=1, padx=5, pady=5,sticky=W+E+N+S)
    b6=Button(main, text="6", relief="flat", bg="lightblue", command=partial(Write, "6"))
    b6.grid(row=4, column=2, padx=5, pady=5,sticky=W+E+N+S)
    bMul=Button(main, text="×", relief="flat", bg="#bbeeff", command=partial(Write, "*"))
    bMul.grid(row=4, column=3, padx=5, pady=5,sticky=W+E+N+S)
    bDiv=Button(main, text="÷", relief="flat", bg="#bbeeff", command=partial(Write, "/"))
    bDiv.grid(row=4, column=4, padx=5, pady=5,sticky=W+E+N+S)
    
    b1=Button(main, text="1", relief="flat", bg="lightblue", command=partial(Write, "1"))
    b1.grid(row=5, column=0, padx=5, pady=5,sticky=W+E+N+S)
    b2=Button(main, text="2", relief="flat", bg="lightblue", command=partial(Write, "2"))
    b2.grid(row=5, column=1, padx=5, pady=5,sticky=W+E+N+S)
    b3=Button(main, text="3", relief="flat", bg="lightblue", command=partial(Write, "3"))
    b3.grid(row=5, column=2, padx=5, pady=5,sticky=W+E+N+S)
    bExp=Button(main, text="^", relief="flat", bg="#bbeeff", command=partial(Write, "^"))
    bExp.grid(row=5, column=3, padx=5, pady=5,sticky=W+E+N+S)
    bSqrt=Button(main, text="√", relief="flat", bg="#bbeeff", command=partial(Write, "√"))
    bSqrt.grid(row=5, column=4, padx=5, pady=5,sticky=W+E+N+S)
    
    b0=Button(main, text="0", relief="flat", bg="lightblue", command=partial(Write, "0"))
    b0.grid(row=6, column=0, padx=5, pady=5,sticky=W+E+N+S)
    bDot=Button(main, text=".", relief="flat", bg="lightblue", command=partial(Write, "."))
    bDot.grid(row=6, column=1, padx=5, pady=5,sticky=W+E+N+S)
    bSign=Button(main, text="+/-", relief="flat", bg="lightblue", command=Sign)
    bSign.grid(row=6, column=2, padx=5, pady=5,sticky=W+E+N+S)
    bEqual=Button(main, text="=", bg="#44ee44", fg="white", relief="flat", command=Print)
    bEqual.grid(row=6, column=3, columnspan=2, padx=5, pady=5,sticky=W+E+N+S)

Components()
main.mainloop()
