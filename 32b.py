
# pattern 1:

for i in range(6):
    for j in range(i):
        print(" ", end="")
    for k in range(6-i):
        print(k+1, end="")
    print()

# pattern 2:

for i in range(6, 0, -1):
    for j in range(6-i):
        print(" ", end="")
    for k in range(i):
        print(k+1, end="")
    print()

# pattern 3:


for i in range(7, 0, -1):
    for j in range(7-i):
        print(" ", end="")
    for k in range(1, i):
        print(k, end="")
    print()

