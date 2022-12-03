print(
    "                                                                            welcome to the game of luck                                                   ")
print("")
print(
    "                                                                                                                              RULES:-  ")
print(
    "                                                                                                                              -> You can choose any random number from 1 to 6")
print(
    "                                                                                                                              -> If you guess the correct number you gain a point")
print(
    "                                                                                                                              -> You can keep going until you want")
print(
    "                                                                                                                              -> Good Luck scoring the Highest (^^)")
import random


def roll_a_dice(x):
    max_value = 6
    min_value = 1
    roll_again = 'yes'
    points = 0
    while roll_again == 'yes' or roll_again == 'y' or roll_again == 'Y' or roll_again == 'Yes' or roll_again == 'YES':
        a = int(input('enter a number between 1 & 6: '))
        print('rolling the dice...')
        b = random.randint(min_value, max_value)
        print('the value is:', b)

        if (a == b):
            points = points + 1
            print('congrats you got it correct and gained a point')
        else:
            print('why not try once more!')
        roll_again = input('roll again?[yes/no]:')

    else:
        c = input(('are you sure you want to exit[yes/no]: '))
        if c == 'no' or c == 'n' or c == 'N' or c == 'NO':
            (roll_a_dice(x))
        else:
            print('your score is: ', points)


z = input('want to roll the dice?[yes/no]: ')
if z == 'yes' or z == 'y' or z == 'Y' or z == 'Yes':
    (roll_a_dice(z))
else:
    print('come if you wanna play')

