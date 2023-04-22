arr = []
temp=0;

arrSize =int(input("Enter the Size: "))

print(f"Enter the {arrSize} numbers")

for i in range(arrSize):
  arr.append(int(input()))

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print()

print("The sorted list is:")
for i in range(0, len(arr)):
    print(arr[i], end=" ")