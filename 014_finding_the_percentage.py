# https://www.hackerrank.com/challenges/finding-the-percentage/problem

# submission 1 - using three variables
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # finding the average
    total = sum(student_marks[query_name])
    num_scores = len(student_marks[query_name])
    average = total / num_scores
    
    # printing the average
    print(f'{average:.2f}')

