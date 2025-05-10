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


# submission 2 - non pythonic solution 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # initializing first max and second max
    first_max = second_max = float('-inf')
     
    # looping through the array
    for num in arr:
        
        # when the current num in the loop is first max
        if num > first_max:
            second_max = first_max
            first_max = num
        
        # when the current num in loop is second max
        elif first_max > num > second_max:
            second_max = num
    
    # print the second max 
    # (edge case if there is no second max is not handled in this solution)
    print(second_max)
