# rec = {}
# rec['name'] = 'mel'
# rec['age'] = 40
# rec['job'] = 'trainer/writer'
#
# print(rec['name'])
#
#
# class rec:
#     pass
#
# rec.name = 'mel'
# rec.age = 40
# rec.job = 'trainer/writer'
#
# print (rec.name)

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def info(self):
        return (self.name, self.job)

rec1 = Person('mel', 'trainer')
rec2 = Person('stas', 'dev')

print(rec1.info())1

