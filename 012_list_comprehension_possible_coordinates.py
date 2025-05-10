# https://www.hackerrank.com/challenges/list-comprehensions/problem

# submission 1 - using for loop inside list comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # using list comprehension to loop through all possibilities 
    # and excluding the non-conforming condition
    print([ 
           [num1, num2, num3] \
           for num1 in range(x+1) \
           for num2 in range(y+1) \
           for num3 in range(z+1) \
           if num1 + num2 + num3 != n 
            ]
    )

