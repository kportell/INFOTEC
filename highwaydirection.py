p = (int(input('Please enter a primary highway number 0-99 : ')))
if p%2==0 :
    print('Highway', p, 'goes east and west')
else :
    print('Highway', p, 'goes north and south')