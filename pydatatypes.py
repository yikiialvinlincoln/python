#datatypes in python
#numeric
#string
#sequence type
#mapping
#boolean
#set

#Numeric; we have integers(int), float(float), complex numbers(complex)
#examples
num1=10
print(num1, "is of a type", type(num1))
num2=150.0
print(num2, "is of a type", type(num2))
num3 = 1+2j
print(num3, "is of a type", type(num3))
num4 = 2+2j
print(num4,"is of a type", type(num4))

#Strings
#a string is a group of characters
name="lincoln" #or name='lincoln'
print(name, "is of a type", type(name))
#semantics is the meaning of what you've written
#typecasting
numx="20"
print(numx, "is of a type", type(numx))
#example of typecasting
numy=str(numx) #conversion of the value of numx into an integer and store it in numy
print(numy, "is of a type", type(numy))
numy=float(numx)
print(numy, "is of a type", type(numy))
numy=int(numx)
print(numy, "is of a type", type(numy))

#sequence data type
#under sequence, we have list, tuples and range
#lists
#a list is a variable that can store more than one value however we can have an empty list meaning we can store values later on
mylist=[]
mylist.append("lincoln")
print(mylist)
mylist.append(15)
print(mylist)
#append is a specialised command we use to give values to a list 
#print is a specialized command in python used to output values on a computer screen
#pop is used to remove the last value of the list
languages=["python","c","c++","c#","swift","julia","ruby","cobol","javascript"]
print(languages[5])
print(languages[0])
print(languages[1])
print(languages[7],languages[4])
print(languages[-1])

country=["uganda","kenya","tanzania",["egypt","somalia",["sudan",["burundi", "nigeria",["togo"],["benin"]]]]]
print(country[3][2][0])
print(country[3][2][1][0])
print(country[3][2][1][1])
print(country[3][0])
print(country[2])
print(country[3][1],country[3][2][0])
print(country[-1][-1][-1][-2][-1])
country.append(10)
print(country)

fruits = ("apples","oranges","mangoes",["pawpaws","pears"])
print(fruits[0])
print(fruits[-2])
print(fruits[3][-1])

#a list is a mutable data type because it can be manipulated after it has been created
#tuples are immutable data types meaning those elements cant be changed
#even tuples can be typecasted thus you can change a tuple into a list but you can't change a list into a tuple

#mapping
person={"name": "Lincoln", "age":24, "country": "Uganda", "height":180}
print(person["country"])
print(person["name"])
print (person.keys())
print (person.values())

student_id= {100, 200, 300, 400, 500,500}
print(student_id)
print (student_id)

list = [1,2,3,4,5,6,7]
list.append(4)
print(list)