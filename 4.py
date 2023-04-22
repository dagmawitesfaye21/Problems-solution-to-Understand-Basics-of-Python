m1=int(input("Insert the slope of the line: "))
b1=int(input("Insert the y-intercept of the line: "))
x1=int(input("Insert the x coordinate value: "))


def Line(m, x, b):
    return (m * x) + b


print(f"the corresponding value of Y for the given value of x is:{Line(m1, b1, x1)}")