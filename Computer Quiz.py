print('Welcome to my computer quiz')
play = input('Do you want to play? ')
if play.casefold() != 'yes':
    quit()
print('Okay, lets play.\n\n')
score = 0
answer = input('What does CPU stand for? ')
if answer == 'Central processing unit'.casefold():
    score += 1
answer = input('What does GPU stand for? ')
if answer == 'Graphic processing unit'.casefold():
    score += 1
answer = input('What does RAM stand for? ')
if answer == 'Random Access Memory'.casefold():
    score += 1
answer = input('What does PSU stand for? ')
if answer == 'Power Supply'.casefold():
    score += 1
print(f'Well done. You got {score}/4 correct.\nYour score is {(score/4)*100}%.')