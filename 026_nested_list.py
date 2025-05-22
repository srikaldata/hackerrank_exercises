# https://www.hackerrank.com/challenges/nested-list/problem


# submission 1 - pythonic solution by sorting and getting all names with second lowest score
if __name__ == '__main__':
    
    # empty list
    students = []
    
    # get the inputs and create a list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # sort the unique scores in ascending order to grab the second lowest
    grades = sorted(set([score for name, score in students]))
    second_lowest = grades[1]
    
    # grabbing the names of 2 or more people with same second lowest score
    result = [name for name, score in students if score == second_lowest]
    result.sort()
    
    # print all the results
    for name in result:
        print(name)
