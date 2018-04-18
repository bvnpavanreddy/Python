class father():
    def gardening(self):
        print("i enjoy gardening")


class mother():
    def cooking(self):
        print("i love to cook for my family")


class child(father,mother):
    def sports(self):
        print("i love cricket")


c= child()
c.gardening()
c.cooking()
c.sports()
    


