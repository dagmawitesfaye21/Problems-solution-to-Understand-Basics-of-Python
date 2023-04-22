def Main():
    # Takes the nine digits as a string separated by space

    print("Enter Nine digits separating by spaces ?")
    digits = list(map(str, input().split()))

    total = 0
    if len(digits) > 9:
        return "You must enter 9 didgits only"

    for i, num in enumerate(digits, 1):
        total += (i * int(num))

    total %= 11
    digits.append(str(total))
    return ("".join(digits))


if __name__ == "__main__":
    print(Main())