#defining an object in python
#we use a keyword class followed by the name of the class identified then ending with a full colon
#a complete fulfillment of attributes form an object 

class Animal: 
    color = ""
    size = ""
    gender = ""
    name = ""
    sound = ""
    species = ""
    age = ""

    def feed(self):
        return "by chewing"  
    

#a function that is defined within a class is called a method
#individual statements within a method are called behaviours

#creating objects of a class Animal
cat = Animal() 
cat.name = "jerry"
cat.color = "white"
cat.size = "medium"
cat.gender = "male"
cat.sound = "meow"
cat.species = "felis catus"
cat.age = "4"
cat.feed()
print(f"{cat.name} feeds {cat.feed} ")    

#accessing objects


#the properties/attributes/features are identified by a dot access specifier
#the +sign is a polymorphic operater

print(cat.name + " does " + cat.sound)

print(cat.name + " is " + cat.color)
print(cat.name + " is " + cat.age + " years old")

print(cat.name + " is " + cat.size)

print(cat.name + " is " + cat.gender)

print(cat.name + " is " + cat.color + " of " + cat.species)

dog = Animal()
dog.name = "tom"
dog.color = "black"
dog.size = "small"
dog.gender = "male"
dog.sound = "barks"
dog.species = "german shepherd"
dog.age = "6"

print(f"{dog.name} is {dog.age} years old")
print(f"{dog.name} is {dog.color}")
print(dog.name + " is " +  " of " + dog.species + " species ")

lion = Animal()
lion.name = "simba"
lion.color = "brown"
lion.size = "big"
lion.gender = "male"
lion.sound = "roars"
lion.species = "panthera leo"
lion.age = "8"

print(f"{lion.name} is {lion.age} years old")
print(lion.name + " is " + lion.size)

print(lion.name + " is " +  " of " + lion.species + " species ")

