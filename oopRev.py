#Basic
class My:
    x = 5

p = My()
print(p.x)

# __init__(automatically called when an object is created, basically a constructor)
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

p1 = Person("eric", 23)
print(p1.name)
print(p1.age)