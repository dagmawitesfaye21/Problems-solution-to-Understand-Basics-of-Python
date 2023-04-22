num1=int(input("insert the Number: "))

def Fibonacci(num):
    if num < 0:
        print("Negative values are not allowed")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)


print(f"the Fibonacci value of the number is: {Fibonacci(num1)}")
