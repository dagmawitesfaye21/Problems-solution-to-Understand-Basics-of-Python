def main():
    num = int(input())
    reverse = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    
    return reverse


print(main())
