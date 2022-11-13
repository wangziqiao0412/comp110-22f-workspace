"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730614342"
guess_1: str = input("Enter a 5-character word:")
guess_2: str = input("Enter a single charcter:")
print("Searching for " + guess_2 + " in " + guess_1)


if len(guess_1) != 5:
    print("Error: Word must contain 5 characters")
    quit()
if len(guess_2) != 1:
    print("Error: Character must be a single character.")
    quit()

i: int = 0
if guess_2 == guess_1[0]:
    print(guess_2 + " found at index 0")
    i += 1
if guess_2 == guess_1[1]:
    print(guess_2 + " found at index 1")
    i += 1
if guess_2 == guess_1[2]:
    print(guess_2 + " found at index 2")
    i += 1
if guess_2 == guess_1[3]:
    print(guess_2 + " found at index 3")
    i += 1
if guess_2 == guess_1[4]:
    print(guess_2 + " found at index 4")
    i += 1
if i > 1:
    print(str(i) + " instances of " + guess_2 + " found in " + guess_1)
elif i == 1:
    print(str(i) + " instance of " + guess_2 + " found in " + guess_1)
else:
    print("No instances of " + guess_2 + " found in " + guess_1)




