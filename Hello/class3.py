class Person:    #The __init__ method is roughly what represents a constructor in Python
    def __init__(self, name, job=None, pay=0):    #constructor take three arguments
        self.name = name                   #Fill out fields when created, self is the new instance object
        self.job = job
        self.pay = pay


if __name__ == '__main__':
    bob = Person('Bob Smith')            # test the class
    sue = Person('Sue Jones', job='dev', pay=100000)     #Runs __init__ automatically\
    print(bob.name, bob.pay)     #Fetch attached attributes, Sue and bob attrs differ
    print(sue.name, sue.pay)