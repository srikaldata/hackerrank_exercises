# https://www.hackerrank.com/challenges/python-lists/problem


# submission 1 - classifying the command and performing the corresponding operations
if __name__ == '__main__':
    N = int(input())
    temp_list = []
    
    # looping through the number of commands
    for _ in range(N):
                    
        # receiving each command from stdin
        command = input().strip().split()
        