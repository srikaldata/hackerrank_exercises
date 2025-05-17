# https://www.hackerrank.com/challenges/designer-door-mat/problem


# submission 1 - using separate for loops for each portion of the mat
# Enter your code here. Read input from STDIN. Print output to STDOUT

# the row by column dimensions
N, M = map(int, input().split())

# top portion of the mat
for i in range(N//2):
    pattern = '.|.'*((2*i)+1)
    print(pattern.center(M, '-'))
    
# middle portion of the mat
print('WELCOME'.center(M, '-'))

# bottom portion of the mat
for i in range((N//2)-1, -1, -1):
    pattern = '.|.' * ((2*i)+1)
    print(pattern.center(M, '-'))
