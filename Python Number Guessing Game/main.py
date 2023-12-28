import random,time

# Functions 

def game(trials):
    # This lines chooses a random number between 1-100
    print("I'll think of a number between 1-100 and you have to guess it in five trials.")
    number= random.randint(1,101)
    user_guess = -1
    while number != user_guess and trials > 0:
        user_guess = int(input("guess>"))

        # block of code compares the guess to the random number and gives the user feedback
        if user_guess > number:
            print(f"Number too high! and you have {trials-1} guesses remaining.")
        elif user_guess < number:
            print(f"Number too low! and you have {trials-1} guesses remaining.")
        elif user_guess == number:
            print(f"Correct!!! And you got it in {5 - trials} guesses.")
            break
        # Removes from the trial after a failed attempt    
        trials -=1
    time.sleep(2) #Adds 2 secs delay to before running the next line
    retry()

# retry function 
def retry():
    ans = input("Play Again?(y/n)").lower() 
    if ans == 'y':
        game(trials)
    else:
        quit()


# Main program        

# Welcome message
print(f"Welcome to number guessing game")
time.sleep(2)


# Variable for how many times the program will run
trials = 5

# the game function is called in the next line
game(trials)
