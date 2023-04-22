a = int(input("Enter First Natural Number : "))
b= int(input("Enter Second Natural Number : "))

if a < 1 or b < 1:
        print("Inputs must be natural numbers (positive integers)")
        
else:
        while b != 0:
            a, b = b, a % b
        
        print("The GCD of Two Natural number is : " , a)