# 5 A function that checks if the two lines intersect or not
def do_lines_intersect(line1, line2):
    # extract the coordinates of line1
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    
    # extract the coordinates of line2
    x3, y3 = line2[0]
    x4, y4 = line2[1]
    
    # calculate the denominator of the equations
    denominator = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    
    # if the denominator is zero, the lines are parallel and do not intersect
    if denominator == 0:
        return False
    
    # calculate the numerators of the equations
    numerator1 = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
    numerator2 = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)
    
    # calculate the parameters of the intersection point
    t1 = numerator1 / denominator
    t2 = numerator2 / denominator
    
    # if the parameters are between 0 and 1, the lines intersect
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        return True
    else:
        return False


print(do_lines_intersect( [[0,0], [5, 5]], [[2,-10], [3, 10]]))
print(do_lines_intersect( [[0,3], [5, 6]], [[27,-10], [1, 10]]))