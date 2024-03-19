#a loop is a mechanism or a way or means of writing instructions to a computer to repeatedly do an action until a certain condition is met
#types of loops; "for" loops and "while" loops
#below we are iterating values in a list of numbers
#for loop
def loop1():
    list = [10, 20, 30, 40, 50, 60]
    for item in list:
        print(item)
def loop2():        
    for i in range(10):
       print(i)
       item = 1   
def loop3():           
    for item in range(1,10):      
        #1 representing the start and 10 being the end point
        #range is a keyword in python
        print(item) 
def loop4():  
    for item in range(1,11):
        print(item)
def loop5():
    for i in range(1,20):
      if i % 2 == 0:
         print(i) 
def loop6():         
    for i in range(1,20):
        if i % 2!= 0:
           print(i)
         #a block of code is a collection of related statements
         #a block of code is identified by indentation

def loop7():         
    digits = [3,6,9,12,15,18,21]
    for i in digits:
        print(i)         
    else:
        print("No items left")
loop1()
loop2()
loop3()
loop4()
loop5()
loop6()
loop7()   
        