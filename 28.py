totalStudent = int(input("What is the total number of students: "))
dictionary = {}
students = []

while totalStudent > 0:
    name = input('Name of the student: ')
    score = int(input('Score of the student: '))
    dictionary[name] = score
    totalStudent -= 1


for key in dictionary:
    students.append(dictionary[key])

print(students)
students.sort()

highest = students[len(students) - 1]
secondHighest = students[len(students) - 2]

print(f"{highest}, {secondHighest}")
