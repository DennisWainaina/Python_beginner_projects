# Program for guessing a number and seeing if the number is correct
# It also subtracts points from 10 and stops if points are at 0 and below
# Such that is stops if the number of tries is 0 or less
import random as rand

random_number = rand.randint(1, 100)
# print('The random number is', random_number)
# print(random_number)
b = [i for i in range(2, random_number) if random_number % i == 0]


tries = 10

while tries > 0:
    guessed_number = int(input('Guess the random number from 1 to 100 ? '))

    if random_number == guessed_number:
        print('You are correct')
        print('You guessed correctly')
        print('The final number of points you have is', tries)
        break

    else:
        print('Not the correct number')
        print('The random number is a multiple of', b)
        print('The number of points you have is', tries - 1)
        print("You're almost there")

    tries = tries - 1
else:
    print('The random number is', random_number)
    print('You failed the guesssing game')
