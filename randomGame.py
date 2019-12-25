#This is a simple

import random
guess_made=0
name=raw_input('hello,what is your name?\n')
number=random.randint(1,20)

print 'well {0},i am thinking a number between 1 and 20.'.format(name)

while guess_made <6:
    guess=int(raw_input('Take a guess:'))
    guess_made +=1
    if guess <number:
        print 'your guess is too low'
    elif guess >number:
        print 'your guess is too high'
    else:
        break

if guess==number:
    print 'good job, {0}!you guessed my number in {1} guesses!'.format(name,guess_made)
else:
    print 'Nope, The number I was thinking of was {0}'.format(number)
                                                                
