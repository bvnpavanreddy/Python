"""class employee:
    raise_amount=1.05
    num_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first +'.'+last+'@company.com'

        employee.num_of_emps +=1

    def fullname(self):
        return '{} {}',format(self.first,self.last)
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amount)
print(employee.num_of_emps)
emp1=employee('john','tom',50000)
emp2=employee('tom','miller',60000)
emp3=employee('alex','john',55000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)

print(emp3.pay)
emp3.apply_raise()
print(emp3.pay)

print(employee.num_of_emps)"""


"""class Account(object):
    def __init__(self, holder, number, balance,credit_line=1500): 
        self.Holder = holder 
        self.Number = number 
        self.Balance = balance
        self.CreditLine = credit_line

    def deposit(self, amount): 
        self.Balance = amount

    def withdraw(self, amount): 
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            return True

    def balance(self): 
        return self.Balance

    def transfer(self, target, amount):
	if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            target.Balance += amount 
            return True"""
        
def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this truck as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the truck."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 10000 - (.10 * self.miles)
