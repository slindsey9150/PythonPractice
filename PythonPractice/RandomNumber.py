import random

# ! Try to guess the computers random number
# x = int(input("Number: "))
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f'Guess a number between 1, and {x}: '))
        if guess < random_number:
            print("sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. too high")
    print(f"Yay congrats! You have guessed the random number and it was {random_number}")

# guess(x)

# ! The computer tries to guess our random number

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f"is {guess} too high (h), too low (l), or correct (c)? ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay the computer guessed my number, {guess} correctly")

computer_guess(1000)