for num in range(1,10): 
    if num > 10:
        print("numbers are out of range")
else: 
    print("the numbers were in range")  
    
myrange = int(input("please enter your range"))
for num in range(1, myrange): 
    if num > 10:
        print("numbers are out of range")
else: 
    print("done")   

num = [1, 2, 3, 4, 5, 6, 7]
for i in num:
    print(i)
else:
    print("no items left")        