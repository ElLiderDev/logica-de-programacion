#Superclase
class Animal:
    def __init__(self,name):
        self.name = name

    def sound():
        pass

#Subclases

class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} Esta Ladrando")

class Cat(Animal):
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} Esta maullando")

my_dog = Dog("Laika")
my_dog.sound()

my_cat = Cat("Manolo")
my_cat.sound()
