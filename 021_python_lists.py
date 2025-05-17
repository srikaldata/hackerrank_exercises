# https://www.hackerrank.com/challenges/python-lists/problem


# submission 1 - classifying the command and performing the corresponding operations
if __name__ == '__main__':
    N = int(input())
    temp_list = []
    
    # looping through the number of commands
    for _ in range(N):
                    
        # receiving each command from stdin
        command = input().strip().split()
        
        # for inserting an elem at an idx
        if command[0] == 'insert':
            temp_list.insert(int(command[1]), int(command[2]))
            
        # printing the list
        elif command[0] == 'print':
            print(temp_list)
        
        # removing the first instance of the specified element
        elif command[0] == 'remove':
            temp_list.remove(int(command[1]))
            
        # appending the given element at the end of the list
        elif command[0] == 'append':
            temp_list.append(int(command[1]))
        