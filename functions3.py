def add(a,b):
    ans = a + b
    print(ans)

age = 25  #this is a global variable that can be accessed anytime within the function
#parameters are inside the parenthesis e.g (a,b) of the function
def add1(a,b):
    ans = a + b + age
    age1 = 100
    print(ans)
    print(age1)
add1(20, 10)    
#print(ans) #this ans variable is out of the scope
#functions are self contained block of code because variables within the function cant be accessed outside the variable except for the global variable


