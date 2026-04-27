import random

red = "\033[91m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

def game():
    
    secret_number = random.randint(1, 100)
    changes = 5
    
    print(f"{yellow} welcome to the hot cold game!{reset}")
    print(f"i chose a number between 1-100. you have {changes} changes.")
    
    guess_number = 0
    won = False

    while changes > 0:
        try:
            print(f"\n remaining changes: {changes}")
            guess = int(input("let's your guess: "))
            
            guess_number += 1
            changes -= 1
            
            difference = abs(secret_number - guess)

            if secret_number == guess:
                print(f"\n{red} congratulations! you found {secret_number} in {guess_number} tries! {reset}")
                won = True
                break
            
            if difference <= 5:
                print(f"{red} very hot! (the difference is 5 or less){reset}")
            elif difference <= 15:
                print(f"{yellow} hot! (the difference is 15 or less){reset}")
            else:
                print(f"{blue} cold! (the difference is more than 15){reset}")
        
        except ValueError: 
            print("please enter only numbers!")

    if not won:
        
        print(f"\n{blue} game over. no changes left. the secret number was {secret_number}. {reset}")

game()

