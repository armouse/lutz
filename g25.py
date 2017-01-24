class C2: pass
class C3: pass

class C1(C2, C3):
    def setname(self, who):
        self.name = who

user1 = C1()
user2 = C1()


user1.setname('Станислав')
user2.setname('Савик')

print(user1.name)
print(user2.name)
