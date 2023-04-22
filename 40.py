firstNum = int(input('Enter the first number: '))
operators = ['/', '*', '-', '+']

for op in operators:
    print(op)

opera = input('Choose an operator: ')
secondNum = int(input('Enter the second number: '))


def sum(firstNum, secondNum):
    return firstNum + secondNum


def difference(firstNum, secondNum):
    return firstNum - secondNum


def product(firstNum, secondNum):
    return firstNum * secondNum


def quotient(firstNum, secondNum):
    return firstNum / secondNum


if opera == "+":
    print(sum(firstNum, secondNum))
elif opera == "*":
    print(product(firstNum, secondNum))
elif opera == '-':
    print(difference(firstNum, secondNum))
elif opera == '/':
    print(quotient(firstNum, secondNum))
else:
    print('Invalid operator')
