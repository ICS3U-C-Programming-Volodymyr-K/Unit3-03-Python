#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 22, 2025
# This program is a immitation of gambling, you need to guess the number from 0 to 9

import random


def main():
    #Gets number from user
    user_number = int(input("Pick number from 0 to 9"))
    #Generates number
    computer_number = random.randint(0, 9)
    #Compares user number with computer generated one
    if user_number == computer_number:
        #Prints the winning the message if numbers are equal
        print("You've guessed correctly.")
    else:
        #Prints lose message if numbers are not equal
        print("Your guess is incorrect, the number is: {}".format(computer_number))


if __name__ == "__main__":
    main()
