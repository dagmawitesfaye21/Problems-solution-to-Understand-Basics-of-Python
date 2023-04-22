num=2388

def is_sum_of_cubes(num):

    total = 0
    for digit in str(num):
        total += int(digit) ** 3
    return total == num


def display_sum_of_cubes(low, high):

    for num in range(low, high+1):
        if is_sum_of_cubes(num):
            print(num)


