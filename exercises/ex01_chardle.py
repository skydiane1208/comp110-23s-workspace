"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730476529"

word: str = input("enter a 5-character word: ")
if len(word) < 5 or len(word) > 5:
    exit(print("Error: Word must contain 5 characters "))
letter: str = input("enter a single character: ")
if len(letter) < 1 or len(letter) > 1: 
    exit(print("Error: Character must be a single character."))
print("searching for " + letter + " in " + word)
count: int = 0
if letter == word[0]:
    print(letter + " found at index 0")
    count = count + 1
if letter == word[1]:
    print(letter + " found at index 1")
    count = count + 1
if letter == word[2]:
    print(letter + " found at index 2")
    count = count + 1
if letter == word[3]:
    print(letter + " found at index 3")
    count = count + 1
if letter == word[4]:
    print(letter + " found at index 4")
    count = count + 1
if count == 0:
    print("No instances of " + letter + " found in " + word)
if count == 1:
    print("1 instance of " + letter + " found in " + word)
if count == 2:
    print("2 instances of " + letter + " found in " + word)
if count == 3:
    print("3 instances of " + letter + " found in " + word)
if count == 4:
    print("4 instances of " + letter + " found in " + word)
if count == 5:
    print("5 instances of " + letter + " found in " + word)