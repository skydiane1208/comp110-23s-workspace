"""EX03 - Wordle """

__author__ = "730476529"

def contains_char(my_words:str, letter_idx: str)-> bool:
    """returns if character in my_words is in letter_idx"""
    assert len(letter_idx) == 1
    letter: int= 0
    while letter < len(my_words):
        if letter_idx == my_words[letter]:
            return True
        else:
            letter= letter+1
    return False 

def emojified(guess_word: str, secret_word: str)-> str:
    """Returns emojis based on if letters in quess are in secret"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess_word) == len(secret_word)
    s: str = ""
    letter: int= 0
    while letter < len(guess_word):
        if guess_word[letter]== secret_word[letter]:
            s += GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[letter]):
                s += YELLOW_BOX
            else:
                s += WHITE_BOX
        letter= letter +1
    return s
            
def input_guess(expected_length: int)-> str:
    guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while (len(guess) != (expected_length)):
        guess = input("That wasn't "+ str(expected_length) + " chars! Try again: ")
    return guess
        
def main()-> None:
    """The entrypoint of the program and main game loop."""
    i: int=1
    game: bool= False 
    secret_word: str = "codes"
    while i <= 6 and game == False:
        print (f"=== Turn {i}/6 === ")
        guess: str = input_guess(len(secret_word))
        print (emojified(guess, secret_word))
        if guess == secret_word:
            game = True
            print(f"You won in {i}/6 turns!")
        else:   
            i+= 1
    if i> 6: 
        print ("X/6 - Sorry, try again tomorrow!")
        
if __name__ == "__main__":
    main()