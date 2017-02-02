class rec:
    pass

rec.name = 'bob'
rec.age = 40


x = rec()
y = rec()

x.name = 'sue'

# print(x.name, y.name, rec.name)

def upperName(self):
    return self.name.upper()

print(upperName(x))

rec.method = upperName

print(x.method())
print(y.method())
