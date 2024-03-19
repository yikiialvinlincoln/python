#a named block of code is called a function
#a function is a group of statements related to one another and performs a specific task
#functions are the building blocks of programming languages
#for example
def myfunction():
    num1, num2 = 20, 40
    print(num1 + num2)
#function call
myfunction()    

#we have 2 types of functions namely static function and dynamic function

#a function is not created but it is defined and thats why its called by def
#from line 15 to line18, its a function definition
#condition
def condition(): 
    num = 10
    if num > 0:
       print("number is positive")
    print("if statement is easy")  
#condition()        
#below code has been extracted from the function itself
num = 10
if num > 0:
   print("number is positive")

#a function is defined by invoking  
condition()   

def mycondition():
    number = -10
    if number > 0:
        print("number is positive")
    else:
        print("number is negative") 
    print("this statement is not related to if or else but in the same function")
    
mycondition()           