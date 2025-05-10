# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# submission 1 - simple pythonic solution using set and max
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # find the unique nums
    set_arr = set(arr)
    
    # remove the max num
    set_arr.remove(max(set_arr))
    
    # apply the max fn again to find the second max
    print(max(set_arr))
    