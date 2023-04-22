stdNum=int(input("Insert the number of student:"))

StudentsGreadDictory = {"Name":[""],"Grade":[0]}
for x in range(0,stdNum):
    name = input("insert student Name: ")
    grade = input("insert student Grade: ")
    StudentsGreadDictory["Name"].append(name)
    StudentsGreadDictory["Grade"].append(grade)

def highestGread():
    max = int(StudentsGreadDictory["Grade"][0]);
    for i in range(0, len(StudentsGreadDictory["Grade"])):
        if int(StudentsGreadDictory["Grade"][i]) > int(max):
            max = StudentsGreadDictory["Grade"][i]
    return max

large=highestGread()

def searchIndex(arr,n,target):
    for j in range(0,n):
        if (int(arr[j])==target):
            return j

n = len(StudentsGreadDictory["Grade"])
ind=searchIndex(StudentsGreadDictory["Grade"],n,int(highestGread()))
print("the maximum grade is: ",large)
print("And it is scored by: ",StudentsGreadDictory["Name"][ind])



















