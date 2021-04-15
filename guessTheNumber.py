import random
number = random.randint(1,9)
count = 1
while(count<=5):
    guessNumber = int (input('Enter Number '))
    if(number == guessNumber):
        print('Your Guess is Correct')
        count = 100
    elif(number<guessNumber):
        print('Guess Lower')
        count = count+1
    elif(number>guessNumber):
        print('Guess Higher')
        count = count+1

if(count != 100):
    print ('Better Luck Next Time')