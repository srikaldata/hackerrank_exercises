# https://www.hackerrank.com/challenges/python-string-formatting/problem


# submission 1 - using str(for decimal) oct hex bin fns and text formatting
def print_formatted(number):
    # your code goes here
    
    # find the width for the space between the values
    width = len(bin(number)[2:])
    
    # for each number generate all 4 values
    for i in range(1, number+1):
        
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        