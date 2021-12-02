import random
roll_again = 'y'
while roll_again == 'y':
    print('Rolling the dice')
    print(random.randint(1,6))
    roll_again = input('Want to roll the dice again (y) or (n) ?  ')