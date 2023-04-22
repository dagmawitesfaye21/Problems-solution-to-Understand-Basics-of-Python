n = int(input("Enter a number: "))
multiple = 1
total = 0
for i in range(n):
    for j in range(i+1):
        multiple *= j + 1
    total = multiple + total
    multiple = 1
print(total)