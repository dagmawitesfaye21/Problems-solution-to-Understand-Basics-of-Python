student = int(input("What is the total number of students: "))
mark = []

while student > 0:
    mark_list = int(input("Insert mark of student out of 30: "))
    mark.append(mark_list)
    student -= 1

count = 0

for num in mark:
    if int(num) > 20 and int(num) <= 30:
        count += 1

print(f"{count} students score more than 20")
