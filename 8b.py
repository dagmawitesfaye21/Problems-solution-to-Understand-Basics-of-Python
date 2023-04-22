num=int(input("Insert the number: "))


def sumofDigits(n):
    n_str = str(n)
    sum = 0
    for i in range(0,len(n_str)):
        sum += int(n_str[i])
    return sum


print(f"the sum of the digit of your number is: {sumofDigits(num)}")
