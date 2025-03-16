import random

secret_number = random.randint(1, 100)

print(secret_number)

number_guessed = False

while number_guessed == False:
    
    try:
        users_guess = int(input("Enter your guess: "))
        if users_guess == secret_number:
            print("correct")
            number_guessed = True
        elif abs(secret_number - users_guess) <=5:
            print("Your really really close")
        elif abs(secret_number - users_guess) <=10:
            print("Your getting warmer")
        elif secret_number > users_guess:
            print("Too Low, try agian")
        else: 
            print("Too High, try agian")
        
    except ValueError:
        print("You must enter a valid number")