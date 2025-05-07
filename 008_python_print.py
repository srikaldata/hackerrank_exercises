# https://www.hackerrank.com/challenges/python-print/problem

# submission 1 - using a for loop
if __name__ == '__main__':
    n = int(input())

    for num in range(1, n+1):
        print(num, end='')


# submission 2 - using a list comprehension
if __name__ == '__main__':
    n = int(input())

    print(*[num for num in range(1, n+1)], sep='')
