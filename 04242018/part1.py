"""class parent:
    def newmethod(self):
        print ("calling the parent class")

class child(parent):
    def newmethod(self):
        print("this is belongs to the child class")

c = child()
c.newmethod()"""

"""class name1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'name1(%d,%d)' %(self.a,self.b)
    def __add__(self,other):
        return name1(self.a+other.a,self.b+other.b)
n1=name1(10,20)
n2=name1(22,-55)
print(n1+n2)"""

"""balance =0

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

print ("total balance" ,deposit(2000))
print("total balance:",withdraw(800))"""


"""def make_account():
    return{'balance':0}
def deposit(account,amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account,amount):
    account['balance'] -= amount
    return account['balance']

a= make_account()
b=make_account()
print("the balance :",deposit(a,2000))
print("the balance :",withdraw(b,500))"""


"""class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

a = BankAccount()
b = BankAccount()

a.deposit(1200)
b.withdraw(500)



class minbalance(BankAccount):
    def __init__(self,minimumbalance):
        BankAccount.__init__(self)
        self.minimumbalance = minimumbalance

    def withdraw(self,amount):
        if self.balance - amount < self.minimumbalance:
            print("sorry you must have minimum balance")
        else:
         BankAccount.withdraw(self,amount)

b= minbalance(500)
b.withdraw(1500)"""
