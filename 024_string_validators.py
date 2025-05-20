# https://www.hackerrank.com/challenges/string-validators/problem

# submission 1 - using print, any and string methods 
if __name__ == '__main__':
    s = input()
    
    # check if the string has any alphanumeric chars
    print(any(str.isalnum(char) for char in s))
    
    # check if the string has any alphabetical chars
    print(any(str.isalpha(char) for char in s))
    