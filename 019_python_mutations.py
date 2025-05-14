# https://www.hackerrank.com/challenges/python-mutations/problem


# submission 1 - converting string to list to string and replacing the character
def mutate_string(string, position, character):
    
    # converting the string to a list
    str_ls = list(string)
    
    # replacing the character at the right position
    str_ls[position] = character
    
    # returning the list of characters as a string
    return ''.join(str_ls)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
