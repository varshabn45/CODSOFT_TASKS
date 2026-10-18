import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)

print("Your choice:" ,user_choice)
print("Computer choice:" ,computer_choice)

if user_choice not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")

elif user_choice == computer_choice:
    print("It's a tie!")

elif (user_choice == "rock" and
computer_choice == "scissors") or \
    (user_choice == "paper" and
computer_choice == "rock") or \
    (user_choice == "scissors" and
computer_choice == "paper"):
    print("Congratulations! You win!")

else:
    print("Computer wins! Better luck next time!")