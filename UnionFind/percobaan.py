# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hoi, mijn naam is', self.name)


p = Person('Nikhil')
p.say_hi()