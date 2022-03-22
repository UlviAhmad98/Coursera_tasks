
# Rock, paper, scissors (conditional statements)

print('''Welcome! Introduce yourself with the basic rules:
Rock destroys the scissors since there is no paper!
Scissors are the enemy of paper if no rock around!
Paper is powerfull as rolling the rock, nothing as being cutted by scissors''')

list=('rock','paper','scissors')

import random

computer_hand=random.choice(list)

user_hand=input('rock, scissors, paper? ')
if user_hand=='x':
    print("See you again!")
        
elif computer_hand==user_hand:
    print('Draw!')
elif computer_hand=='rock' and user_hand=='paper':
    print('You are goddamn on fire!')
    print('Computer choosed ' + computer_hand)
elif computer_hand=='paper' and user_hand=='scissors':
    print('You are goddamn on fire. Congrats!')
    print('Computer choosed ' + computer_hand)
elif computer_hand=='scissors' and user_hand=='rock':
    print('You are goddamn on fire. Congratulations!')
    print('Computer choosed ' + computer_hand)
else:
    print('Computer kicked you so hard!')
    print('Computer choosed ' + computer_hand)

