hr = float(input("Enter hr"))
rate = float(input("Enter rate"))

if hr <= 40:
    pay = hr*rate
elif hr > 40:
    pay = ((hr-40)*rate*1.5)+(40*rate)
print(pay)