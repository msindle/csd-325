"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""


# CHANGED: Added bonus rule,
#          updated intro text to explain the new mon bonus.
#          updated house fee from 10% to 12%
#          changed prompts to reflect new house fee
#          added new prompt for when player wins the new mon bonus

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, modified by Michael Sindle

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NOTE: If the dice total is 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('mns: ')   # CHANGED: Prompt uses initials
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.\n')
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('mns: ').upper()  # CHANGED: Prompt uses initials
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    total = dice1 + dice2

    # ADDED: Bonus rule
    if total == 2 or total == 7:
        print(f"You rolled a total of {total}! You get a 10 mon bonus!")
        purse += 10

    rollIsEven = (total % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        house_fee = int(pot * 0.12)  # CHANGED: 12% house fee
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
