
def euler_formula(x):
    e = 2.71828  
    result = 1.0 
    term = 1.0  
    i = 1  
    while term > 1e-10: 
        term *= x / i 
        result += term  
        i += 1  
    return result  

x = float(input("Enter x: "))
e_to_x = euler_formula(x)
print("e^x =", e_to_x)
