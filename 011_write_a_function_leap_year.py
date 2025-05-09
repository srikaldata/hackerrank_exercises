# https://www.hackerrank.com/challenges/write-a-function/problem

# submission 1 - using if else
def is_leap(year):
    leap = False
    
    # Write your logic here
    # div by 4 and not div by 100
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    
    # div by 400
    elif year % 400 == 0:
        leap = True

    return leap

