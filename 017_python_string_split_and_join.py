# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

# submission 1 - using split and join string methods
def split_and_join(line):
    # write your code here
    line = line.split(' ')
    line = '-'.join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# submission 2 - using replace string method
def split_and_join(line):
    # write your code here
    return line.replace(' ', '-')

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
