"""EX06 - Choose Your Own Adventure."""
__author__ = "730614342"
import random
points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U0001f600"


def greet() -> None:
    """Greeting players who join in this game."""
    global points, player
    print(f"{NAMED_CONSTANT} Welcome to the game!") 
    player = input('Plz enter your name:\n') 


def reassign_score() -> None:
    """Giving players initial points."""
    global points
    action: int = int(input(f"{player} you have three choices:\n1. Pikachu \n2. Bulbasaur \n3. Squirtle \nPlease input the index of your choice:\n"))
    if action == 1:
        points = 1
    elif action == 2:
        points = 2
    elif action == 3:
        points = 3
    else:
        print('Invalid action number!')


def interaction_score(input_points: int) -> int:
    """Giving players points according to their choice."""
    global points, player
    interaction: int = int(input(f"{player}, you have three choices:\n1. adventure \n2. food \n3. home \nPlease input the index of your choice:\n"))
    if interaction == 1: 
        adventure_points = random.randint(-2, 6)
        input_points += adventure_points 
    elif interaction == 3:
        input_points += 3
    elif interaction == 2:
        food_num: int = int(input(f"{player}  you have three choices:\n1. apple \n2. orange \nPlease input the index of your choice:\n"))
        if food_num == 1:
            input_points += 1 
        elif food_num == 2:
            input_points += 2
        else:
            print('Invalid food number!')
    else:
        print('Invalid action number!')
    return input_points


def main() -> None:
    """Let's begin the game."""
    global points, player
    greet()
    while True:
        user_choice = int(input(f"{player}, you have three choices:\n1. select a new pet \n2. action \n3. end the game \nPlease input the index of your choice:\n"))
        if user_choice == 1:
            reassign_score()
            print(f'{NAMED_CONSTANT} Your current adventure points is:{str(points)}')
        elif user_choice == 2:
            points = interaction_score(points)
            print(f'{NAMED_CONSTANT} Your current adventure points is:{str(points)}')
        elif user_choice == 3:
            print(f'{NAMED_CONSTANT} Goodbye! Your final adventure points is:{str(points)}!')
            break
        else:
            print('{NAMED_CONSTANT} Invalid choice number!Plz choose again')


if __name__ == "__main__":
    main()