import random

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0
    
    while True:
        print("Rock, Paper, Scissors")
        print("Enter your choice (rock, paper, scissors) or 'q' to quit:")
        user_choice = input().lower()
        
        if user_choice == 'q':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        # Generate computer's choice
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
        
        print("Score: User -", user_wins, "Computer -", computer_wins, "Draws -", draws)
        print()

# Start the game
play_game()
