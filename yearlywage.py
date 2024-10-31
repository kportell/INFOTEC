hours = float(input('Enter hours worked per day: '))
rate = float(input('Enter rate of pay: '))
rateb = (rate * 2)
days = 365
pay = hours * rate * days + (hours-8) * rateb * days
if hours > 8 :
    print('You will be compensated for overtime')
print(pay)