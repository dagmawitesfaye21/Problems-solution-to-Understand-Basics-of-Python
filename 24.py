n=int(input("inter any number:"))
sum1=0
for i in range(1,n):
    if(n%i ==0):
        print(i)
        sum1+=i
if(sum1==n):
    print("perfect")
else:
    print("not perfect")