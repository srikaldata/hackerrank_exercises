# https://www.hackerrank.com/challenges/find-a-string/problem


# submission 1 - pythonic version using a counter and for loop
def count_substring(string, sub_string):
    
    # counter
    count = 0
    
    # substring length
    sub_string_len = len(sub_string)
    
    # looping through each char in the string
    for i in range((len(string)-sub_string_len)+1):
        
        # count if the substring is found
        if string[i:(i+sub_string_len)] == sub_string:
            count += 1

    return count
