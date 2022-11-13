
"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730614342"
guess: str = input("What is your 6-letter guess?")
secret = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i = 0
while len(guess) != 6:
    guess_again = input("That was not 6 letter! Try again:")
while i < len(secret):
    if guess[i] == secret[i]:
        print(GREEN_BOX, end="")
    else:
        k = 0
        while k < len(secret):
            if guess[i] == secret[k]:
                print(YELLOW_BOX, end="")
                break
            k = k + 1
        else:
            print(WHITE_BOX, end="")
    i = i + 1
if guess == secret:
    print("\nWoo! You got it!")
else:
    print("\nNot quite. Play again soon!")



    