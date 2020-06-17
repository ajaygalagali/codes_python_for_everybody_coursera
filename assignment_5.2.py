



minNumber = 0
maxNumber = 0
i = 0
flag = True
while flag is True:
    try:
        number = input("Enter number :")
    except:
        pass
    if number == "done":
        print(maxNumber)
        print(minNumber)
        flag = False
    elif number.isdigit():
        if i == 0:
            minNumber = int(number)
            i += 1
        if number != "done":
            number = int(number)
            if number > maxNumber:
                maxNumber = number
            elif number < minNumber:
                minNumber = number
    else:
        print("Invalid op")





