
def main():
    ask_user = True
    while True:
        user_choice = str(input('Convert fahrenheit to celsius (continue or done)'))
        if user_choice == 'done':
            print('Good bye!')
            break
        if user_choice != ('continue' or 'done'):
            print('Invalid answer please try again')
            break
        else:
            tempf = float(input('what is the temp in fahrenheit: '))
        if tempf < -459.67:
            print('invalid number')
        if tempf > -459.67:
            c=(tempf-32)*5/9
            print('The temperature in celsius is',c,'degrees')

main()
    




