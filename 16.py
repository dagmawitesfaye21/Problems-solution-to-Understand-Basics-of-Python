
previous_num = 1
total_sum = 0

for num in range(3, 100, 2):
    total_sum += (previous_num/num)
    previous_num = num

print(total_sum)