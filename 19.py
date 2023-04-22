  
ans = []
for year in range(2001, 2101):
    if (year % 100 == 0) and (year % 400 == 0):
        ans.append(year)
    elif year % 4 == 0:
        ans.append(year)

for i in range(len(ans)):
    if i != 0  and i%10 == 0:
        print()
    print(ans[i], end=" ")
