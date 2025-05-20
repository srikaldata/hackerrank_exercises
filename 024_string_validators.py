# https://www.hackerrank.com/challenges/string-validators/problem

# submission 1 - using print, any and string methods 
if __name__ == '__main__':
    s = input()
    
    # check if the string has any alphanumeric chars
    print(any(str.isalnum(char) for char in s))
    
    # check if the string has any alphabetical chars
    print(any(str.isalpha(char) for char in s))
    
    # check if the string has any digit chars
    print(any(str.isdigit(char) for char in s))
    
    # check if the string has any lowercase chars
    print(any(str.islower(char) for char in s))
    
    # check if the string has any uppercase chars
    print(any(str.isupper(char) for char in s))


# submission 2 - using list of str methods and a for loop
if __name__ == '__main__':
    s = input()
    
    # list of functions to be applied on the string
    fn_list = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    
    # printing the result of checks after applying the string based methods
    for fn in fn_list:
        print(any(fn(char) for char in s))
