
"""EX03 - Structured Wordle"""
__author__ = "730614342"


def contains_char(a: str, b: str) -> str:
    """Confirm that whether a is including b."""
    assert len(b) == 1
    i = 0
    while i < 3:
        if b == a[i]:
            return True
        i = i + 1
    else:
        return False # why always be none???


def emojified(guess: str, secret: str) -> str:
    """Using green, yellow, and grey to test the word."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    k = 0
    y = 0
    while y < 5:
        if guess[y] == secret[y]:
            print(GREEN_BOX, end="")
        else:
            while k < 5:
                if guess[y] == secret[k]:
                    print(YELLOW_BOX, end="")
                    break
                k = k + 1
            else:
                print(WHITE_BOX, end="")
    y = y + 1

def input_guess(expected_length: int) -> int:
    """Find a X character word."""
    entered = input("Enter a " + expected_length + " character word:")
    while len(entered) != expected_length:
        entered = input("That wasn't" + str(expected_length) + " chars! Try again:")
