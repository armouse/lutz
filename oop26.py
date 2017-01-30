class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class Seconclass(FirstClass):
    def display(self):
        print('Curent value = "%s"' % self.data)

class ThirdClass(Seconclass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass %s]' % self.data
    def mul(self, other):
        self.data *= other

a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
print(a)
