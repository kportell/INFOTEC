hours = int(input('Enter hours worked\n'))
rate = float(input('Enter rate of pay\n'))
pay = hours * rate
if hours <= 40 :
    print(pay)
else:
    print(pay * 2)
    print('You will be compensated for working overtime')
