
def Main(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
        decimal //= 16
    print(f"0x{hexadecimal}")

if __name__ == "__main__":
    decimal = int(input("Enter a decimal integer: "))
    Main(decimal)