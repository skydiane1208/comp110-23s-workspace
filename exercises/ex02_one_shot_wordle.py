"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730476529"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
while (len(guess) != 6):
    guess = input("That was not 6 letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
search_guess: int = 0
s: str = ""
while search_guess < 6:
    if guess[search_guess] == secret_word[search_guess]:
        s = s + GREEN_BOX
        search_guess += 1
    else: 
        search_word: int = 0
        found: bool = False
        while (found is False and search_word < 6):
            if guess[search_guess] == secret_word[search_word]:
                found = True
            else:
                search_word += 1
        if found is True:
            s = s + YELLOW_BOX
            search_guess += 1
        else:
            s = s + WHITE_BOX
            search_guess += 1
if guess == secret_word:
    print(s)
    print("Woo! You got it!")
else:
    print(s)
    print("Not quite. Play again soon!")