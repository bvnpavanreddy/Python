class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp1=employee('john','miller',50000)
print(emp1.fullname)
print(emp1.email)
