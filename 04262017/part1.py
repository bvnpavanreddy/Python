

"""class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=self.first + '.' +self.last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1=employee('tom','jenny',50000)
emp2=employee('mukesh','ambani',90000)

print(employee.fullname(emp1))
print(emp1.email)"""



class employee:
    raise_amount=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+ last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def pay_rise(self):
        self.pay=int(self.pay*self.raise_amount)

class developer(employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lan):
        #employee.__init__(self,first,laast,pay)or
        super().__init__(first,last,pay)
        self.prog_lan=prog_lan

class manager (employee):

    def __init__(self,first,last,pay,prog_lan,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rempve_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())

    
        


emp1=developer('john','michel',60000,'python')

mng1=manager('tom','kyle',70000,[emp1])
print(mng1.email)
print(developer.fullname(emp1))
print(emp1.email)

print(emp1.pay)
#emp1.pay_rise()
#mng1.pay_rise()
mng1.add_emp(emp1)
print(mng1.pay)
#print(emp1.pay)
#print(emp1.prog_lan)
mng1.print_emps()

#print(help(developer))

print (isinstance(mng1,manager))

print(issubclass(employee,manager))

print(issubclass(manager,employee))

