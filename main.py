def username(name):
    if name == 'admin':
        return 'Hello', name
    else:
        return 'error'

print(username('admin'))

a = 3
b = 5
if a > b:
    print a
else:
    print b

