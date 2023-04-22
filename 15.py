def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a*b)//gcd(a,b)


num1 = int(input("Enter the first natural number: "))
num2 = int(input("Enter the second natural number: "))

result = lcm(num1, num2)

print("The least common multiple of", num1, "and", num2, "is", result)
