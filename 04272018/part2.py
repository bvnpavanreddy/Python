"""class vehicle(object):

    base_sales_price=0
    
    def __init__(self,wheels,make,year,sold_on,miles,model):
        self.wheels=wheels
        self.make=make
        self.year=year
        self.sold_on=sold_on
        self.miles=miles
        self.model=model

    def sale_price(self):
        if self.sold_on is not none:
            return 0.0
        return 5000.0*self.wheels
    def purchase_price(self):
        if self.sold_on is none:
            return 0.0
        return self.base_sales_price-(.10*self.miles)

class car(vehicle):
    def __init__(self,wheels,make,year,sold_on,miles,model):
        self.wheels=wheels
        self.make=make
        self.year=year
        self.sold_on=sold_on
        self.miles=miles
        self.model=model
        self.base_sales_price=8000
class truck(vehicle):
    def __init__(self,wheels,make,year,sold_on,miles,model):
        self.wheels=wheels
        self.make=make
        self.year=year
        self.sold_on=sold_on
        self.miles=miles
        self.model=model
        self.base_sales_price=10000"""



class Dog:

    
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)



jim = Bulldog("Jim", 12)
print(jim.description())


print(jim.run("slowly"))


print(isinstance(jim, Dog))


julie = Dog("Julie", 100)
print(isinstance(julie, Dog))


johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))


print(isinstance(julie, jim))
    
