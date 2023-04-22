
# Pattern 1:

for i in range(1, 7):
    for j in range(1, 7-i):
        print(' ', end='')
    for k in range(i, 0, -1):
        print(k, end='')
    print()

  # Pattern 2: 
 
for i in range(1, 7):
    for j in range(1, 7):
        if j >= 7 - i:
            print(7 - j, end="")
        else:
            print(" ", end="")
    print()



