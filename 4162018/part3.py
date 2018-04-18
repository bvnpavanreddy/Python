class father():
    def skills (self):
        print("i enjoy gardening and programming ")


class mother():
    def skills(self):
        print("i enjoy cooking and painting")

class child(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("i love sports")

c = child()
c.skills()
