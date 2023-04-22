def isPrime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def main():
    num = int(input())

    if isPrime(num):
        print("PRIME")
    else:
        print("NOT PRIME")

main()
