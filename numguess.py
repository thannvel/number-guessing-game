import random

random_number = random.randint(1,50)
attempts_left = 5
print("The game starts! You'll have five attempts to guess the correct number.")

while attempts_left > 0:
    try:
        guess = int(input("\nType your guess:"))
    except ValueError:
        print("\nType a number in the right way, please.")
        continue

    if guess == random_number:
        print("Congrats, you won!")
        break
    elif guess < random_number:
        print("Guess higher.")
    elif guess > random_number:
        print("Guess lower.")

    attempts_left -= 1
    print(f"You've {attempts_left} attemts left.")
    
if attempts_left == 0:
    print("\n\nUnfortunately, the game's over.")
    print(f"The correct answer was {random_number}.")