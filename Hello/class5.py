class Person:  # The __init__ method is roughly what represents a constructor in Python
    def __init__(self, name, job=None, pay=0):  # constructor take three arguments
        self.name = name  # Fill out fields when created, self is the new instance object
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    bob = Person('Bob Smith')  # test the class
    sue = Person('Sue Jones', job='dev', pay=100000)  # Runs __init__ automatically\
    print(bob.name, bob.pay)  # Fetch attached attributes, Sue and bob attrs differ
    print(sue.name, sue.pay)
    print(bob.lastname(), sue.lastname())  # Extract last name
    sue.giveraise(.10)
    print(sue.pay)
