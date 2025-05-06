# https://www.hackerrank.com/challenges/a-very-big-sum/problem

# submission 1 - simple pythonic solution
def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)

# submission 2 - non pythonic using for loop
def aVeryBigSum(ar):
    # Write your code here
    total = 0
    for num in ar:
        total += num
    return total
