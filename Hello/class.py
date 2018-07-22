class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveraise(self, percent, bonus=.10):
        self.person.giveraise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastname(), sue.lastname())
    sue.giveraise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveraise(.10)
    print(tom.lastname())
    print(tom)
