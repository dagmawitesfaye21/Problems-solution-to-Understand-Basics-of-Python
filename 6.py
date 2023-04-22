num=int(input("Insert the Number: "))


def factorial(num1):
    if num1 > 0:
        if num1 == 1 or num1 == 0:
            return 1
        else:
            return num1 * factorial(num1 - 1)
    else:
        print("Insert Positive Integer!!!")


print(f"the factorial of the number is: {factorial(num)}")