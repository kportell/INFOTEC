import random

print('Winning rules of the game Rock Paper Scissors are :\n'
      + 'Rock vs Paper -> Paper envelopes Rock!\n'
      + 'Rock vs Scissors -> Rock smashes Scissors!\n'
      + 'Paper vs Scissors -> Scissors cuts Paper!\n')

while True:
    print('Enter your choice \n 1 - Rock \n 2 - Paper \n 3 = Scissors \n')
    while True:
        try:
           choice = int(input('Enter your choice: '))
        except ValueError:
            print('Please enter a number 1-3')
            continue
        else:
            break
           
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is: ', choice_name)
    print('Now its the computers turn')
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print('Computer choice is: ', comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        result = 'Draw'
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'
    
    if result == 'Draw':
        print('<== Its a tie! ==>')
    elif result == choice_name:
        print('<== User Wins! ==>')
    else:
        print('<== Computer Wins! ==>')

    print('Do you want to play again? (y/n)')
    ans = input().lower()
    if ans == 'n':
        break
print('Thanks for playing!')
