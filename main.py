def username(name):
    if name == 'admin':
        return 'Hello', name
    else:
        return 'error'

print(username('admin'))



