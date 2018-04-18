class vehicle:
    def general_usage(self):
        print("general use: transportation purpose")


class car(vehicle):
    def __init__(self):
        print("i am a car")
        self.wheels = 4
        self.has_roof= True

    def specific_usage(self):
        self.general_usage()
        print("Specific usage: commute to work, vacation with family")


class motorcycle(vehicle):
    def __init__(self):
        print("i am motor cycle")
        self.wheels =2
        self.has_roof=False

    def specific_usage(self):
        self.general_usage()
        print("specific usagge: road trip and for racing")


c= car()
c.specific_usage()

m= motorcycle()
m.specific_usage()

print (issubclass(car,vehicle)) # if you wanted to know which calss is subclass of which class or not we can use this class 
