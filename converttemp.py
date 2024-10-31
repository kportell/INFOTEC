
def main():
    ask_user = True
    while True:
        user_choice = str(input('Do you want to convert celsius to fahrenheit?'))
        if user_choice == 'no':
            break
        if user_choice != ('yes' or 'no'):
            print('Please enter yes or no')
            break
        else:
            temp = float(input('what is the temp in celsius: '))
        if temp < -459.67:
            print('invalid number')
        if temp > -459.67:
            f=(temp*1.8)+32
            print('The temperature in fahrenheit is',f,'degrees')

main()
    




