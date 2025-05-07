# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

# submission 1 - using 3 print statements
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)


# submission 2 - using 1 print statement
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b, a-b, a*b, sep='\n')
