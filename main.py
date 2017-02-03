from person import Person
bob = Person('Bob Smith')

# print(bob)
# print(bob.__class__)
# print(bob.__class__.__name__)
# print(list(bob.__dict__))

for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])