# https://www.hackerrank.com/challenges/py-if-else/problem

# submission 1 - using if and elif  
if __name__ == '__main__':
    n = int(input().strip())
    
    # odd check
    if n % 2 == 1:
        print('Weird')
    
    # even check
    elif n % 2 == 0:
        
        # even and between 2 and 5
        if n in list(range(2,6)):
            print('Not Weird')
        
        # even and between 6 and 20
        elif n in list(range(6,21)):
            print('Weird')
        
        # even and greater than 20
        elif n > 20:
            print('Not Weird')


# submission 2 - using if elif and else
if __name__ == '__main__':
    n = int(input().strip())
    
    # odd check
    if n % 2 == 1:
        print('Weird')
    
    # even check
    else:
        
        # even and between 2 and 5
        if n in range(2,6):
            print('Not Weird')
        
        # even and between 6 and 20
        elif n in range(6,21):
            print('Weird')
        
        # even and greater than 20
        else:
            print('Not Weird')
