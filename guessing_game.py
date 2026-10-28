print("Welcome to a guessing game where you have to guess a secret number in 5 attempts!")
secret_number = 33
attempts = 5

for i in range(attempts):
    lives_remaining = attempts - i
    guess = int(input(f"Enter your guess! (Lives Remaining: {lives_remaining}):"))
    if guess == secret_number:
       print("You guessed it! Congratulations!")
       break
    elif guess > secret_number:
        print("Oohhh!Your guess is too high.")
    else:
        print("Oohhh!Your guess is too low")
else:
    print(f"Oh man!It's Game Over and u couldnt guess the secret number. Well now i can tell you that the secret number was...{secret_number}")