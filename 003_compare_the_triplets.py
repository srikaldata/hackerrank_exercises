# submission 1 - using for loop
def compareTriplets(a, b):
    # Write your code here
    
    # initializing the points earned 
    points = [0,0]
    
    # loop through each element
    for i in range(len(a)):
        
        # when a element is greater
        if a[i] > b[i]:
            points[0] += 1
            
        # when b element is greater
        elif a[i] < b[i]:
            points[1] += 1
        
        # when a and b elements are equal
        elif a[i] == b[i]:
            continue
    
    return points


alice = [10,10,10,12]
bob = [9,10,11,10]

print(compareTriplets(alice, bob))

# submission 2 - without the equal condition
def compareTriplets(a, b):
    # Write your code here
    
    # initializing the points earned 
    points = [0,0]
    
    # loop through each element
    for i in range(len(a)):
        
        # when a element is greater
        if a[i] > b[i]:
            points[0] += 1
            
        # when b element is greater
        elif a[i] < b[i]:
            points[1] += 1

    return points

print(compareTriplets(alice, bob))

# submission 3 - using zip and list comprehension
def compareTriplets(a, b):
    # Write your code here
    
    # a points
    a_points = sum([ elem_a > elem_b for elem_a, elem_b in zip(a, b) ])
    
    # b points
    b_points = sum([ elem_a < elem_b for elem_a, elem_b in zip(a, b) ])
    
    return [a_points, b_points]

print(compareTriplets(alice, bob))
