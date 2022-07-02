class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, char):
        if self.age > char.age:
            print("{} is younger than me.".format(char.name))
        elif self.age < char.age:
            print("{} is older than me.".format(char.name))
        else:
            print("{} is the same age as me.".format(char.name))

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

p1.compare_age(p2)
p2.compare_age(p1)
p1.compare_age(p3)
p2.compare_age(p3)
p3.compare_age(p1)
p3.compare_age(p2)