"""ask user for number give hints about number if wrong"""

SECRET: int = 10
guess: int = int(input("guess a number!"))
playing: bool = True

while playing:
    if guess == SECRET:
        print("Correct! you did ir! belive in you dreams <3")
        playing = False
    else:
        if guess % 2 == 1:
            print("your guess is odd.the answer is even.")
        if guess > SECRET:
            print("too high")
        if guess < SECRET:
            print("too low")
        guess = int(input("wrong guess try again!"))
        