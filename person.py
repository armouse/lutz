class Person:
    def __init__(self, name, pay=0, job=None):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, pay, job='mgr')
    # def giveRaise(self, percent, bonus=.10):
    #     Person.giveRaise(self, percent+bonus)



class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Person('Tod Beners', pay=50000)

development = Department(bob,sue)
development.addMember(tom)
development.giveRaises(.10)
development.showAll()

1



# if __name__ == '__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     tod = Person('Tod Beners', pay=50000)
#     print('--All three--')
#     for object in (bob, sue, tod):
#         object.giveRaise(.10)
#         print(object)
#
#     print(tod.job)





    # print(bob)
    # print(sue)
    # print(bob.lastName(), sue.lastName())
    # sue.giveRaise(.10)
    # print(sue.pay)
    # print(sue)
    # tod.giveRaise(.10)
    # print(tod.lastName())
    # print(tod)

