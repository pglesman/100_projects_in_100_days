import random
import art

print(art.logo)
print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

number = random.randint(1, 100)
difficulty = ''
attempts = {
    'easy': 10,
    'hard': 5,
}

while difficulty not in ('easy', 'hard'):
    difficulty = input("Choose a difficulty. Type \'easy\' or \'hard\': ")

for attempt in range(attempts[difficulty], 0, -1):
    if attempt > 1:
        print(f'You have {attempt} attempts remaining to guess the number.')
    else:
        print(f'You have {attempt} attempt remaining to guess the number.')

    guess = int(input("Make a guess: "))

    if guess == number:
        print(f'You got it! The answer is {number}.')
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

    if attempt > 1:
        print("Guess again.")

else:
    print("You've run out of guesses, you lose.")
