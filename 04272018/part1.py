"""class parent:
    def mymethod(self):
        print('this is parent calss')

class child(parent):
    def mymethod(self):
        print('this is child classs')



p=parent()
c = child()

c.mymethod()
p.mymethod()"""


"""def scope_test():
    def do_local():
        spam="local spam"

    def non_local():
        nonlocal spam
        spam='nonlocal spam'

    def do_global():
        global spam
        spam='global spam'

    spam = "test spam"
    do_local()
    print("after local :",spam)
    non_local()
    print("after non local",spam)
    do_global()
    print("after global:",spam)

scope_test()
print("in global scope:",spam)"""


"""class Dog:

    tricks = []            

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.add_trick('roll over'))
print(e.add_trick('play dead'))"""


class car(object):
    def __init__(self,wheels,miles,make,model,year,sold_on):
        self.wheels=wheels
        self.miles=miles
        self.make=make
        self.model=model
        self.year=year
        self.sold_on=sold_on

    def sales_price(self):
        if self.sold_on is not none:
            return 0.0
        return 5000.0 * self.wheels
    def purchase_price(self):
        if self.sold_on is none:
            return 0
        return 8000 -(-.10 * self.miles)

class Truck(object):
    def __init__(self,wheels,miles,make,model,year,sold_on):
        self.wheels=wheels
        self.miles=miles
        self.make=make
        self.model=model
        self.year=year
        self.sold_on=sold_on

    def sales_price(self):
        if self.sold_on is not none:
            return 0.0
        return 5000.0 * self.wheels
    def purchase_price(self):
        if self.sold_on is none:
            return 0
        return 15000 -(-.10 * self.miles)
             


    
