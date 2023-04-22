n= int(input('enter number: '))
count=0
for i in range(2, n+1):
    sqrt_num = int(i**(0.5))
    for j in range(2, sqrt_num+1):
        if i%j == 0:
            break
    else:
        count+= 1
print(count,"Prime Numbers")
