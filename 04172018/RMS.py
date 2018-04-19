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


f2 = Frame(root,width = 800, height= 700 , relief=SUNKEN)
f2.pack(side=LEFT)# left frame
# now we need to decide on which we need to put what

f3 = Frame(root,width = 300, height= 700, relief=SUNKEN)
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

def ref():
    x=random.randint(1,5050500)
    randomref=str(x)
    rand.set(randomref)

    COF = float(Fries.get())
    COD = float(Drinks.get())
    COB = float(Burger.get())
    CostofFilet = float(Filet.get())
    COChicken = float(Chicken.get())
    COCheese = float(Cheese.get())


    CostofFries = COF*0.99
    CostOfDrinks = COD*1.00
    CostOfBurger = COB*2.87
    CostofFilet = CostofFilet*2.99
    CostOfChicken = COChicken*2.89
    CostOFCheese_Burger = COCheese*2.69

    CostOfMeal ="$", str('%.2f' % (CostofFries+CostOfDrinks+CostOfBurger
                                   +CostofFilet+CostOfChicken+CostOFCheese_Burger))
    payTax=((CostofFries+CostOfDrinks+CostOfBurger
                                   +CostofFilet+CostOfChicken+CostOFCheese_Burger)*0.2)
    TotalCost = (CostofFries+CostOfDrinks+CostOfBurger
                                   +CostofFilet+CostOfChicken+CostOFCheese_Burger)
    Service_Charge = ((CostofFries+CostOfDrinks+CostOfBurger
                                   +CostofFilet+CostOfChicken+CostOFCheese_Burger)/99)
    Service = "$",str('%.2f' %Service_Charge)
    OverAllCost="$",str('%.2f' %(payTax+TotalCost+Service_Charge))
    PaidTax = "$",str('%.2f' %payTax)

    Service_Charge.set(Service_Charge)
    Cost_of_meal.set(CostOfMeal)
    State_Tax.set(PaidTax)
    SubTotal.set(CostOfMeal)
    TotalCost.set(OverAllCost)
    

def Exit():
    root.destroy()

def Reset():
    
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Chicken.set("")
    Cheese.set("")
    Drinks.set("")
    Cost.set("")
    Service_Charge.set("")
    State_Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    
    

txtDisplay=Entry(f3,font=('arial',20,'bold'),textvariable=text_input,bd=30,
                 insertwidth=4,bg="#ffffff",justify='right')

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
#---------------------------------------------Restaurant Info1--------------------------------------------

rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
Chicken=StringVar()
Cheese=StringVar()
Drinks=StringVar()
Cost=StringVar()
Service_Charge=StringVar()
State_Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()

lblReference= Label(f2, font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f2,font=('arial',16,'bold'),textvariable=rand,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtReference.grid(row=0,column=1)


lblFries= Label(f2, font=('arial',16,'bold'),text="Large Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f2,font=('arial',16,'bold'),textvariable=Fries,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtFries.grid(row=1,column=1)


lblBurger= Label(f2, font=('arial',16,'bold'),text="Burger Meal",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f2,font=('arial',16,'bold'),textvariable=Burger,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtBurger.grid(row=2,column=1)


lblFilet= Label(f2, font=('arial',16,'bold'),text="Filet Meal",bd=16,anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f2,font=('arial',16,'bold'),textvariable=Filet,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtFilet.grid(row=3,column=1)


lblChicken= Label(f2, font=('arial',16,'bold'),text="Chicken Meal",bd=16,anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f2,font=('arial',16,'bold'),textvariable=Chicken,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtChicken.grid(row=4,column=1)


lblCheese= Label(f2, font=('arial',16,'bold'),text="Cheese Meal",bd=16,anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f2,font=('arial',16,'bold'),textvariable=Cheese,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtCheese.grid(row=5,column=1)

#---------------------------------------------Restaurant Info2--------------------------------------------


lblDrinks= Label(f2, font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f2,font=('arial',16,'bold'),textvariable=Drinks,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtDrinks.grid(row=0,column=3)


lblCost= Label(f2, font=('arial',16,'bold'),text="Cost of Meal",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f2,font=('arial',16,'bold'),textvariable=Cost_of_meal,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f2, font=('arial',16,'bold'),text="Service Charge",bd=16,anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f2,font=('arial',16,'bold'),textvariable=Service_Charge,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f2, font=('arial',16,'bold'),text="State Tax",bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f2,font=('arial',16,'bold'),textvariable=State_Tax,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtStateTax.grid(row=3,column=3)


lblSubTotal= Label(f2, font=('arial',16,'bold'),text="SubTotal",bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f2,font=('arial',16,'bold'),textvariable=SubTotal,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtSubTotal.grid(row=4,column=3)


lblTotalCost= Label(f2, font=('arial',16,'bold'),text="Total Cost",bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f2,font=('arial',16,'bold'),textvariable=TotalCost,bd=16,
                 insertwidth=4,bg="#ffffff",justify='right')
txtTotalCost.grid(row=5,column=3)

#=====================================================Buttons================================

btnTotal=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="Total",bg="powder blue",command=ref).grid(row=7,column=1)

btnReset=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="Exit",bg="powder blue",command=Exit).grid(row=7,column=3)



root.mainloop()
