import random

random_num = random.randint(1, 9)

user_guess = input('Guess a number between 1 and 9: ')

if (int(user_guess) > random_num):
    print('Too high')
elif (int(user_guess) < random_num):
    print('Too low')
elif (int(user_guess) == random_num):
    print('You guessed it!')

print('User guess is: ', user_guess)

print('random number is: ', random_num)
