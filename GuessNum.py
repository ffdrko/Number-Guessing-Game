import random as r


def guessNum(level):
    if level == 'easy':
        live = 10
        while live >= 1:
            user_guess_num = int(input("I'm thinking of a number between 1 and 100.\n=>"))
            if user_guess_num == computer_guess:
                print(f"The number {user_guess_num} is a correct guess.")
                print("You Win.")
                break
            else:
                live -= 1
                print(f"You have {live} chances to guess.")
                if user_guess_num > computer_guess:
                    print(f"The number is lower then {user_guess_num}")
                else:
                    print(f"The number is greater then {user_guess_num}")
    elif level == 'hard':
        live = 5
        while live >= 1:
            user_guess_num = int(input("Guess a number between 1 and 100.\n=>"))
            if user_guess_num == computer_guess:
                print(f"The number {user_guess_num} is a correct guess.")
                print("You Win.")
                break
            else:
                live -= 1
                print(f"You have {live} chances to guess.")
                if live == 0:
                    print("You lost")
                    print(f"The actual guess number was {computer_guess}")
                if user_guess_num > computer_guess:
                    print(f"The number is lower then {user_guess_num}")
                else:
                    print(f"The number is greater then {user_guess_num}")
    else:
        print("This is not a correct action. Please type accordingly.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
user_game_level =input("Chose a difficulty.Type 'easy' or 'hard'!\n=>").lower()

computer_guess = r.randint(1, 101)
guessNum(user_game_level)