import random

print("Welcome to Rock-Paper-Scissors Game")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    print("Oh! Thanks for joining in")
    quit()

print("Okay good! Let's play :)")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please choose Rock, Paper or Scissors. If you want to quit the game, type Q: ")

    if user_input.lower() == "q":
        break

    if user_input.lower() not in options:
        print("Please choose among Rock, paper and Scissors only")
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + ".")

    if user_input.lower() == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins +=1

    elif user_input.lower() == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins +=1

    elif user_input.lower() == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins +=1

    else:
        print("You lost!")
        computer_wins +=1

print("Thankyou! for playing the game.")
print("You won",user_wins,"times.")
print("The computer won",computer_wins,"times.")
print("GoodBye!")