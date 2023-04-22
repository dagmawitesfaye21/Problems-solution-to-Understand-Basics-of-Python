def max_number(nums):
    frequency = [[0,i] for i in range(max(nums)+1)]

    for num in nums:
        frequency[num][0] += 1

    frequency.sort()
    return frequency[-1]

nums = list(map(int,input("Enter numbers: ").split()))
occurrence,max_num = max_number(nums)
print("The largest number is ",max_num)
print("The occurrence count of the largest number is ",occurrence)

