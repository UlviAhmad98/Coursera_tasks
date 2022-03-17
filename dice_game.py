player1=input('First player should enter the name:\n')
player2=input('Second player should enter the name:\n')

import random
def roll_dice():
    dice_game=random.randint(1,11)+random.randint(1,11)
    return dice_game

roll1=roll_dice()
roll2=roll_dice()

if roll1==roll2:
    print('Nice draw')
if roll1>roll2:
    print(player1, 'won')
if roll1<roll2:
    print(player2, 'won')

