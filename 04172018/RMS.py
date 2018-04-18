from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0") # this is for size of the window
root.title("Restaurant Management Systems") # this is to give a title fot the app

text_input =StringVar()
operator=""
# now define three frames

f1 = Frame(root,width = 1600, height = 50,bg="powder blue", relief=SUNKEN)
f1.pack(side=TOP)# this is for the top frame


f2 = Frame(root,width = 800, height= 700 ,bg="powder blue", relief=SUNKEN)
f2.pack(side=LEFT)# left frame
# now we need to decide on which we need to put what

f3 = Frame(root,width = 300, height= 700,bg="powder blue", relief=SUNKEN)
f3.pack(side=RIGHT)

#=======================Time=================================================
localtime = time.asctime(time.localtime(time.time()))
#===============================info==========================================
lblinfo= Label(f1, font=('arial',50,'bold'),text="Restaurant Management Systems",fg="Steel Blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

lblinfo= Label(f1, font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblinfo.grid(row=1,column=0)

#===============================Caliculator=============================
def btnclick(numbers):
    global operator 
    operator = operator + str(numbers)
    text_input.set(operator)

def clearbtn():
    global operator 
    operator = ""
    text_input.set("")

def equlabtn():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
    

txtDisplay=Entry(f3,font=('arial',20,'bold'),textvariable=text_input,bd=30,
                 insertwidth=4,bg="powder blue",justify='right')

txtDisplay.grid(columnspan=4)

btn7=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=2,column=0)
btn8=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda:btnclick(8)).grid(row=2,column=1)
btn9=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda:btnclick(9)).grid(row=2,column=2)
addition=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=2,column=3)
#-----------------------------------------------------------------------------------------------

btn4=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column=0)
btn5=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column=1)
btn6=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column=2)
substraction=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column=3)

#----------------------------------------------------------------------------------------------
btn1=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=4,column=0)
btn2=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=4,column=1)
btn3=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=4,column=2)
multiply=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column=3)

#----------------------------------------------------------------------------------------------------
btn0=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column=0)

clear=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="c",bg="powder blue",command=clearbtn).grid(row=5,column=1)

equals=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=equlabtn).grid(row=5,column=2)
division=Button(f3,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column=3)


root.mainloop()
