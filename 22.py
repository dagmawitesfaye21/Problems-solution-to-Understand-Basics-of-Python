def main():
    num = int(input())

    while num >= 0:
        numberOfDigits = 0

        temp = num
        count = 0
        while temp > 0:
            temp //= 10
            count += 1
        
        print(count)
        num = int(input())

main()
        