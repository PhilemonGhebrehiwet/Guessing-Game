import random


def guess_int(prompt):
    while True:
        tempt = input(prompt)
        if tempt.isnumeric():
            return int(tempt)
        else:
            print('{} is not a valid number.'.format(tempt))


answer = random.randint(1, 10)
guess = guess_int('Guess my number between 1 and 10: ')
counter = 1
if guess == answer and counter <= 1:
    print('Lucky Guess')
while guess != answer:
    if guess == 0:
        print('Game Over')
        quit()
    elif guess < answer:
        print('Too low')
    elif guess > answer:
        print('Too high')
    guess = guess_int('Guess Again: ')
    counter += 1
else:
    if counter > 1:
        print('Correct')
print('You got it in {} attempts.'.format(counter))
