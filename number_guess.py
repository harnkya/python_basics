# python random module
# generate a random number between 1-100
# want user to guess the number and ask with how many guesses will user find the number.
# mark the user according to guess number over 100

# Also randint() could have been used for this question.


import random

game_over = False
while not game_over:
    number = random.randrange(1, 101)
    print("Number has generated.")

    guess_num = int(input("Please enter the number of guess: "))
    lost = True

    for i in range(guess_num):
        user_guess = int(input("Enter your guess:"))
        if number > user_guess:
            print("Up")
        elif number < user_guess:
            print("Down")
        else:
            print(f"Congrats! You found the number with {i+1}th guess.")
            point = (100/guess_num)*(guess_num-i)
            print(f"Your point is {point}")
            lost = False
            break
    if lost:
        print("You lost!!! Ran out of guesses.")

    if input("Do you want to continue?[y/n] ").lower() == "n":
        game_over = True
