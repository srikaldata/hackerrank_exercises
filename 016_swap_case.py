# https://www.hackerrank.com/challenges/swap-case/problem

# submission 1 - pythonic solution using string method swapcase
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
