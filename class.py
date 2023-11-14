# class.py

class Person:
    def __init__(self):
        self.name = "default_name"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p1.name = "Ian Lim"
p1.print()

p2 = Person()
p2.print()

Person.title = "new_title"
print(p1.title)
print(p2.title)
print(Person.title)