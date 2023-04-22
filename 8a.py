num=int(input("Insert the number: "))
if num == 1:
    print("the number is neither prime nor composite")
else:
    def is_prime(n, i=2):
        if n < 2:
            return False
        elif i * i > n:
            return True
        elif n % i == 0:
            return False
        return is_prime(n, i + 1)
    if is_prime(num):
        print("the number is Prime")
    else:
        print("The number is Composite ")





