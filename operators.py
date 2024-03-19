#An operator
name = "lincoln"
#an operator is a special character that tells a computer what to do with the value and an operand is what a computer acts upon
#operator symbols and their meaning
#arithmetic operators(+, -, *, /, //)
num1 = 100
num2 = 200
sum = num1 + num2
print(sum)
#subtraction
sub = num1 - num2
print(sub)
#multiplication
mul = num1 * num2
print(mul
)
#division
div = num1 / num2
print(div)

#floor division
floordiv = num2 // num1
print(floordiv)
floordiv = num1 // num2
print(floordiv)

#exponential/power(**)
print(num1**2)
print(4**3)

#modulo 
#it returns the remainder of one number divided by another
print(num1 % num2)

#assignment operators
#equal sign
num3 = num1 + num2
#addition assignment operator
num1 += 2 #num1 = num1 + 2
print(num1)
#subtraction assignment operator
num1 -= 2  #num1 = num1 - 2
print(num1)
#multiplication assignment operator
num1 *= 2 #num1 = num1 * 2
print(num1)
#division assignment operator
num1 /= 2 #num1 = num1 / 2
print(num1)
#exponential division assignment operator
num1 **= 2 #num1 = num1 ** 2
print(num1)
#modulo assignment operator
num1 %= 2 #num1 = num1 % 2
print(num1)

#Boolean data types
#comparison operators(true/false, yes/no)
#these comparison operators compare two values and return a true or false result
comp1 = 100
comp2 = "lincoln"
print(comp1 == comp2)
#two equal signs are used to compare two values
#you start with !=
print(comp1 != comp2)

#greater than/less than
print(num1 < num2)
print(num1 > num2)

#greater than or equal to
print(10 >= 20)

#logical "and"
print(True and True)
print(True and False)

#logical "or"
print(True or False)
print(False or True)

#logical "not"
print(not True)

#membership operators(in/out)
mylist = [10, 20, 30, 40, 50]
print(10 in mylist)
print(100 in mylist)
print(100 not in mylist)

#identity operators
mylist2 = [10, 20, 30, 40, 50]
print(mylist is not mylist2)
print(mylist is mylist2)

#a statement that evaluates to a value is called an expression
#a value in programming is called an operand
#an operator acts upon an operand

#loops and conditions
#repeatedly do something until the condition is false

print(False and False)
print(True and False)
print(False and True)