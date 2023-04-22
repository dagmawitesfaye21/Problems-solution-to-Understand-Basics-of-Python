choice = int(input('to convert kilograms to pounds enter 1, to convert miles to kilometer enter 2, to convert hours to minutes enter 3: '))
if(choice == 1):
    kilogram = int(input("Enter the kilogram to change to pound: "))
    pound = kilogram * 2.20462
    print(round(pound, 2))
elif(choice == 2):
    mile = int(input("Enter the mile to change to kilometer: "))
    kilometer = mile * 1.60934
    print(round(kilometer, 2))
elif(choice == 3):
    hour = int(input("Enter the hour to change to minute: "))
    minute = hour * 60
    print(minute)