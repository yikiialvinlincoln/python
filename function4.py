def vat(rate, price):
    frate = int((rate/100) * price)
    print(frate)
    return frate 
print(vat(18, 20000))

def actualprice():
    actvat = vat(18, 20000)
    print(actvat) 
    netprice = actvat + 20000
    print(netprice) 
actualprice()  

#a function that wants to share a particular value must return that value to any calling function in otherwords making it global 
#a return function exposes a function outside the value
#the values you pass to the parameters when invoking a function are called arguments eg. rate and price are parameters to the function
#return is the last statement they will execute in a function ie even if you put other things below a statement, they will not include them

#assignment 
#using parameterised functions, create at least 3 functions that share values, the two functions should be dynamic, the last function should be receiving values from the previous functions and printed out

#assignment
#what are your new learning takeaways with examples in code from the time we last had our first assignment