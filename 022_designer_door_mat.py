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


# submission 2 - using only one for loop
# Enter your code here. Read input from STDIN. Print output to STDOUT

# the row-by-column dimensions
N, M = map(int, input().split())

for row in range(N):
    
    # designing and printing the center portion
    if row == N//2:
        print('WELCOME'.center(M, '-'))
        
    # designing and printing the top or bottom portions
    else:
        # calculating pattern repetitions based on the row
        pattern_reps = ((2*row)+1) if row < N//2 else (2*(N-row-1)+1)
        print(('.|.' * pattern_reps).center(M, '-'))
    