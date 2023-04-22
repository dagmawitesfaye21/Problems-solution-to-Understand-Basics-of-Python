isZero = False
number = []

posNum = 0
negNum = 0

while not isZero:
    num = int(input('Enter an int number, the program exists if the input is "0": '))
    number.append(num)
    if num == 0:
        isZero = True
        print(number)
        for numb in number:
            if numb > 0:
                posNum += 1
            elif numb < 0:
                negNum += 1

totalNum = posNum + negNum + 1
totalSum = sum(number)


print(f"The number of positives is {posNum}")
print(f"The number of negatives is {negNum}")
print(f"The total is {totalNum}")
print(f"The average is {totalSum / totalNum }")
