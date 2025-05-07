# https://www.hackerrank.com/challenges/python-division/problem

# submission 1 - using 2 print statements
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)


# submission 2 - using 1 print statement
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b, a/b, sep='\n')
