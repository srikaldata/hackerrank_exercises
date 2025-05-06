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


# submission 3 - non pythonic using while loop
def aVeryBigSum(ar):
    # Write your code here
    total = 0
    idx = 0
    while idx < len(ar):
        total += ar[idx]
        idx += 1
    return total


example_ls = [1,2,3,4,5]

print(aVeryBigSum(example_ls))
