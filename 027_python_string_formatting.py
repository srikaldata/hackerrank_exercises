# https://www.hackerrank.com/challenges/python-string-formatting/problem


# submission 1 - using str oct hex bin fns and text formatting
def print_formatted(number):
    # your code goes here
    
    # find the width for the space between the values
    width = len(bin(number)[2:])
    