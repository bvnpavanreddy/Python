from tkinter import *
myGui = Tk()

def hello():
    b = a.get()
    myLabel3 = Label(text=b,fg='red',bg='yellow',font='10').pack()
def dele():
    myLabel4 = Label(text='Deleted',fg='red',bg='yellow',font='10').pack()
def newfi():
    myLabel4 = Label(text='Clicked on New File',fg='red',bg='yellow',font='10').pack()

a = StringVar()

myGui.title("Hello")
myGui.geometry("500x500+100+200")
myLabel1 = Label(text='lable one',fg='red',bg='yellow',font=('arial',15,'italic')).pack()
mybutton1 = Button(text='submit',fg='red',bg='yellow',command=hello,font='10').pack()
text = Entry(textvariable = a).pack()
mybutton2 = Button(text='Recet',fg='black',bg='green',command=dele,font='10').pack()
mymenu = Menu()

listone=Menu()
listone.add_command(label='New',command=newfi)
listone.add_command(label='Open')
listone.add_command(label='Save')

listtwo=Menu()
listtwo.add_command(label='Cut')
listtwo.add_command(label='copy')
listtwo.add_command(label='Paste')

formatlist=Menu()
formatlist.add_command(label='Intent')
formatlist.add_command(label='Delete')
formatlist.add_command(label='Comment')

Runlist=Menu()
Runlist.add_command(label='Python')
Runlist.add_command(label='Check')
Runlist.add_command(label='Run')

Optionslist=Menu()
Optionslist.add_command(label='Configure')
Optionslist.add_command(label='Code')


Windowlist=Menu()
Windowlist.add_command(label='ZoomIn')
Windowlist.add_command(label='ZoomOut')


mymenu.add_cascade(label="file",menu=listone)
mymenu.add_cascade(label="Edit",menu=listtwo)
mymenu.add_cascade(label="Format",menu=formatlist)
mymenu.add_cascade(label="Run",menu=Runlist)
mymenu.add_cascade(label="Options",menu=Optionslist)
mymenu.add_cascade(label="Window",menu=Windowlist)
mymenu.add_cascade(label="Help")
myGui.config(menu=mymenu)



myGui.mainloop()
 
