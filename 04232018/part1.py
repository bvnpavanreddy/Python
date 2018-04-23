"""emp={'tom':123,'john':124,'alex':1234}
def test(emp):
    new ={'kyle':12345,'jabin':123456}
    emp.update(new)
    print ("this is inside the function",emp)
    return
test(emp)
print ("this is out side of the function",emp)"""


"""import math
print(dir(math))"""

"""class employee:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount +=1

    def displaycount(self):
        print("total employees are :",employee.empcount)

    def displayemp(self):
        print("Name:",self.name,"Salary:",self.salary)
        
emp1=employee("Tom",5000)
emp2=employee("john",10000)
emp1.displaycount()
emp1.displayemp()"""


"""class empexp:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        empexp.empcount +=1

    def displaycount(self):
        print("Total employees are %d" % empexp.empcount)

    def displayemp(self):
        print("Name:",self.name,"Salary:",self.salary)

emp1=empexp("tom",3000)
emp2=empexp("alex",2500)

print ("Employee.__doc__:",empexp.__doc__)
print ("Employee.__name__:",empexp.__name__)
print ("Employee.__module__:",empexp.__module__)
print ("Employee.__bases__:",empexp.__bases__)
print ("Employee.__dict__:",empexp.__dict__)

"""      

"""class Point:
    def __init( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
    
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts)"""


class Parent:
    parentAttr = 100
    def __init__(self):
    print ("Calling parent constructor")
    def parentMethod(self):
        print ('Calling parent method')
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)
class Child(Parent): # define child class
    def __init__(self):
        print ("Calling child constructor")
    def childMethod(self):
        print ('Calling child method')
c = Child() 
c.childMethod() 
c.parentMethod()
c.setAttr(200) 
c.getAttr() 
