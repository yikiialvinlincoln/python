def tests(test1, test2):
    #this function compares scores of two tests and returns the higher one 
    if test1 == test2:
        #if the two scores are equal, return either one of them
        return test1
    else:
        #if the two scores are not equal, return the higher score
        return test2
#this prompts me to insert the marks for test two

test2 = int(input('Please enter Marks for test two: '))

'''
there should also be a test one variable that prompts me to insert marks for test one

'''
def courseWrk(cswork):
    #this function calculates the final coursework marks
    testsMark = tests(test1,test2)
    #it calculates the average of the coursework and the test marks
    avgtestsCswork = (cswork + testsMark)/2
    #this calculates the final test and coursework marks as an average of 40%
    fnltestsCswork = avgtestsCswork * (40/100)
    #outputs the final test and coursework marks
    print('..............................')
    #this outputs the final coursework marks
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
#this prompts me to input the coursework marks
cswork = int(input('Please enter your course work Marks: '))
#this call function calculates and outputs the coursework marks
courseWrk(cswork)