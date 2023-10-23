# A class is a blueprint of an object
# Objects are instances of a class

class Person:
    name = "Ian"
    age = 20
    gender = "Male"

    def walk(self):
        print("Walking")

p = Person()
p.walk()

print(p.name)