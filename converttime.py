hour = int(input('What is the hour: '))

if hour > 11 :
    ampm = "pm"
else:
    ampm = "am"
    
if hour < 0 or hour > 23 :
    print('Please enter a valid hour')
    quit()
if hour == 0 :
    hour = 12
if hour in range(13,23):
    hour = (hour - 12)
    
minute = int(input('What is the minute: '))
if minute < 0 or minute > 59 :
    print('Please enter a valid minute')
    quit()


    
print(hour, minute, ampm)
