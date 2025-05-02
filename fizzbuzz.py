# fizzbuzz submission 1 - using for loop
for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz", end="")
        if num % 5 == 0:
            print("Buzz", end="")
    elif num % 5 == 0:
        print("Buzz", end="")
    else:
        print(num, end="")
    print('')

# fizzbuzz submission 2 - using while loop
num = 1
while num <= 100:
    if num % 3 == 0:
        print("Fizz", end="")
        if num % 5 == 0:
            print("Buzz", end="")
    elif num % 5 == 0:
        print("Buzz", end="")
    else:
        print(num, end="")
    print('')
    num+=1
