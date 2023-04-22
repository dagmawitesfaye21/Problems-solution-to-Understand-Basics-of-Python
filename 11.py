num=[0]*9;
print("insert the number with space between each digit \n")
mobNum=input()
arr=mobNum.split(" ")
if len(arr)==9:
    for x in range(0, len(arr)):
        intArr = int(arr[x])
        num[x] = intArr
    if num[0] == 9:
        print("mobile")
    else:
        print("fixed phone")
elif len(arr)!=9:
    print("the number is too short or too long")



