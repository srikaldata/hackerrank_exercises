# https://www.hackerrank.com/challenges/python-loops/problem

# submission 1 - using a for loop
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)


# submission 2 - using a list comprehension
if __name__ == '__main__':
    n = int(input())
    
    print(*[i**2 for i in range(n)], sep='\n')
