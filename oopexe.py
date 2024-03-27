#define 5 classes with at least shish method taking about 5 paramaters and create at least 3 objects out of those classes
class Person:
    def __init__(self, name, gender, age, location, size):
        self.name = name
        self.gender = gender
        self.age = age
        self.location = location
        self.size = size
person1 = Person("alvin", "male", "24", "ntinda", "slender")   
print(person1.name, person1.gender, person1.age, person1.location)  


class Dog:
    def __init__(linc, name, gender, age,species, size):
        linc.name = name
        linc.gender = gender
        linc.age = age
        linc.species = species
        linc.size = size
dog1 = Dog("spike", "male", "6","german shepard", "big")
print(dog1.name, dog1.gender, dog1.age, dog1.species)

class Benz:
    def __init__(self, model, color, fuel, engine, shape):
        self.model = model
        self.color = color
        self.fuel = fuel
        self.engine = engine
        self.shape = shape
mybenz = Benz("ML350", "black", "diesel", "v6", "suv")
print(mybenz.model, mybenz.engine)

class House:
    def __init__(self, type, location, size, color, roofing):
        self.type = type
        self.location = location
        self.size = size
        self.color = color
        self.roofing = roofing
house1 = House("flat", "valley", "huge", "white", "tiled")

class Samsung:
    def __init__(alvin, name, storage, color, condition, simpacks):
        alvin.name = name
        alvin.storage = storage
        alvin.condition = condition
        alvin.color = color
        alvin.simpacks = simpacks
mysamsung = Samsung("S23", "256gb", "matte black", "brand new", "single slot")        

#the shish function is called a constructor
#it is used to initialize an instantiate object
#the shish function is used to give values to an object
