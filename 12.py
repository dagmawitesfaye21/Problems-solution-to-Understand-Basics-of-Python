size = int(input("Enter the size of the list: "))
myList=[]
for i in range(size):
    num = int(input("Enter a number: "))
    myList.append(num)

maximum = max(myList)    
minimum = min(myList)

print("Maximum number is: ", maximum)
print("Minimum number is: ", minimum)