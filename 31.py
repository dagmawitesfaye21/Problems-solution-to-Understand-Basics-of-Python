start_char = ord('!')
end_char = ord('~')
count = 0

for i in range(start_char, end_char+1):
    print(chr(i), end=' ')
    count += 1
    if count == 10:
        print()
        count = 0
