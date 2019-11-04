# Brett Roach
# 6907380

def num_chars(listOfStr): 
    ''' 
    (10 points) 
    Function that takes in a list of strings (listOfStr) and returns 
    the number of characters for all characters in the strings in 
    listOfStr. 
    - Returns -1 if listOfStr is not a list type or if any element in 
    listOfStr is not a string type.
    - Note: There are many ways to do this and returning -1 is known 
    as a *sentinel* value, which is a value that should not occur. In 
    this case, having -1 as a character count signals the caller of 
    the function that something went wrong (since it doesn't make 
    sense for a character count to be negative). This is not the only 
    way to communicate an incorrect state (there are better ways to 
    handle errors like this), but we will use a *sentinel* value for 
    this function. 
    ''' 
    if type(listOfStr) != list:
        return -1
    else:
        sumOfList = 0
        for item in listOfStr:
            if type(item) != str:
                return -1
            else:
                sumOfList += len(item)
        return sumOfList

def compute_factorial(n):
    '''
    Input a non-negative integer n and return the value of n factorial
    (n!, which is n*(n-1)*...*1, so 3! is 3*2*1).
    - If n is negative or not an int type, return the *sentinel* value
    of -1
    - Your solution should use a `for` loop.
    - Hint: note that 0! = 1. You may have to adjust your range in your
    for loop to account for this.
    '''
    if type(n) != int or n < 0:
        return -1
    else:
        nFactorial = 1
        for x in range(1, n+1):
            nFactorial = nFactorial * x
        return nFactorial

def get_max(listOfNums):
    '''
    Input a list of numbers (listOfNums) and return
    the maximum value in the list.
    - Returns the None type if listOfNums is not a list, if listOfNums
    does not have elements in the list, or if an element in listOfNums
    is not a numerical type (int or float).
    Note: This is an example of using Python's None type as a
    *sentinel* value.
    - Your solution should use a `for` loop and not use the max()
    function.
    - Hint: You can assign a default maxValue variable as
    the 1st element of listOfNums (if valid).
    You can then iterate through listOfNums and compare the current
    maxValue with each element in the list, updating maxValue if needed.
    '''
    if type(listOfNums) != list:
        return None
    else:
        if type(listOfNums[0]) == int or type(listOfNums) == float:
            maxValue = listOfNums[0]
        for num in listOfNums:
            if type(num) != int and type(num) != float:
                return None
            elif num >= maxValue:
                maxValue = num
        return maxValue

def get_index(value, listOfValues):
    '''
    Input a value (of any type) and a list of values of any type
    (listOfValues). Return the index in the list of
    the first match between value and an element in listOfValues.
    - Returns None if listOfValues is not a list type.
    - Returns -1 if value is not found in the list.
    '''
    if type(listOfValues) != list:
        return None
    elif value not in listOfValues:
        return -1
    else:
        return listOfValues.index(value)
                
                





