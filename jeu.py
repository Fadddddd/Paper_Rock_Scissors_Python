import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("rock, paper or scissors?: ")
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("It's a tie!")
    elif player == "rock":
        print("computer: ", computer)
        print("player: ", player)
        if computer == "paper":
            print("You lose")
        elif computer == "scissors":
            print("You win!")
    elif player == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        if computer == "paper":
            print("You win!")
        elif computer == "rock":
            print("You lose!")
    elif player == "paper":
        print("computer: ", computer)
        print("player: ", player)
        if computer == "scissors":
            print("You lose!")
        elif computer == "rock":
            print("You win!")
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again != "yes":
        break
print("Bye")
