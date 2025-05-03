# submission 1 - using in built sum function
ar = [1,2,3,4,5, 1]
print(sum(ar))


# submission 2 - using for loop 
def simpleArraySum(ar):
    # Write your code here
    # instantiating the result variable
    result = 0
    
    # adding each element in the list with the result variable
    for elem in ar:
        result += elem
        
    return result

print(simpleArraySum(ar))
