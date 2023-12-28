from time import sleep
import os

def countdown():
    # Takes the time from user in seconds
    count = int(input("Time in seconds> "))
    
    # Create a for loop to count the number
    for i in range(count):
        # Makes the for loop count down
        print(count - i)
        # pause the program for 1 seconds to simulate the time
        sleep(1)
        # Clear the screen to  make the countdown show in a particular line continously
        os.system('cls' if os.name == 'nt' else 'clear')

    print("Time's up!")
    retry()


def retry():
    ans = input("Try Again?(y/n)").lower() 
    if ans == 'y':
        countdown()
    else:
        print("Goodbye!")
        sleep(1)
        #clears the terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #ends the program
        quit()

countdown()