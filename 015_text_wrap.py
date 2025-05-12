# https://www.hackerrank.com/challenges/text-wrap/problem

# submission 1 - using textwrap.fill method
import textwrap

def wrap(string, max_width):
    
    # using textwrap.fill method 
    return textwrap.fill(string, width = max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    