
n = int(input("Enter a number: "))
length = 1
c = n
for i in range(n):
    mid = length // 2
    j, count = 0, 1
    level = []
    for i in range(c):
        print(" ",end=" ")
    while j <  mid + 1:
        level.append(count)
        count *= 2
        j += 1
    
    reverselevel = level[::-1]
    reverselevel = reverselevel[1:]
    level.extend(reverselevel)
    print(*level)
    
    length += 2
    c -= 1
    