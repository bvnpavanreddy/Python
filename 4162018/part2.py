class human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays Tennis")
        elif self.occupation == "Actor":
            print(self.name,"shoots films")
    def speaks(self):
        print (self.name,"says how are you")

tom=human("Tom Cruise","Actor")
tom.do_work()
tom.speaks()

sharapova = human("maria sharapova","tennis player")
sharapova.do_work()
sharapova.speaks()
        
