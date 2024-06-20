# write a welcome message for a paper rock scissors game
print('Welcome to Paper Rock Scissors!')

# add variables to track the number of wins and rounds
wins = 0
rounds = 0

# add a while loop that runs as long as the user does not enter 'q'
while True:
    # write a message to the console asking the user if they want to play by entering 'p' for play or 'q' for quit
    print('Enter p to play or q to quit')

    # wait for user input p or q
    user_input_to_play = input()

    # if the user enters 'p' then write 'Great! Let's play!' to the console
    if user_input_to_play == 'p':
        print('Great! Let\'s play!')
    # if the user enters 'q' then write 'Goodbye!' to the console and stop the while loop
    elif user_input_to_play == 'q':
        print('Goodbye!')
        # if number of rounds is greater than 0 then write the number of wins and rounds to the console
        if rounds > 0:
            print(f'You won {wins} out of {rounds} rounds')
        break
    # if the user enters anything else then write 'Invalid input' to the console
    else:
        print('Invalid input')
        continue

    # increment the number of rounds
    rounds += 1

    # write a message to the console asking the user to enter 'r' for rock, 'p' for paper, or 's' for scissors
    print('Enter r for rock, p for paper, or s for scissors')

    # wait for user input r, p, or s
    user_input = input()

    # if the user enters 'r' then write 'You chose rock' to the console
    if user_input == 'r':
        print('You chose rock')
    # if the user enters 'p' then write 'You chose paper' to the console
    elif user_input == 'p':
        print('You chose paper')
    # if the user enters 's' then write 'You chose scissors' to the console
    elif user_input == 's':
        print('You chose scissors')
    # if the user enters anything else then write 'Invalid input' to the console
    else:
        print('Invalid input')

    # compute a random choice for the computer
    import random
    computer_choice = random.choice(['r', 'p', 's'])

    # if the computer chooses 'r' then write 'The computer chose rock' to the console
    if computer_choice == 'r':
        print('The computer chose rock')
    # if the computer chooses 'p' then write 'The computer chose paper' to the console
    elif computer_choice == 'p':
        print('The computer chose paper')
    # if the computer chooses 's' then write 'The computer chose scissors' to the console
    elif computer_choice == 's':
        print('The computer chose scissors')

    # if the user and computer both choose the same thing then write 'It's a tie!' to the console
    if user_input == computer_choice:
        print('It\'s a tie!')

    # if the user chooses 'r' and the computer chooses 's' then write 'You win!' to the console
    elif user_input == 'r' and computer_choice == 's':
        print('You win!')
        wins += 1
    # if the user chooses 'p' and the computer chooses 'r' then write 'You win!' to the console
    elif user_input == 'p' and computer_choice == 'r':
        print('You win!')
        wins += 1
    # if the user chooses 's' and the computer chooses 'p' then write 'You win!' to the console
    elif user_input == 's' and computer_choice == 'p':
        print('You win!')
        wins += 1
    # if the computer chooses 'r' and the user chooses 's' then write 'You lose!' to the console
    elif computer_choice == 'r' and user_input == 's':
        print('You lose!')
    # if the computer chooses 'p' and the user chooses 'r' then write 'You lose!' to the console
    elif computer_choice == 'p' and user_input == 'r':
        print('You lose!')
    # if the computer chooses 's' and the user chooses 'p' then write 'You lose!' to the console
    elif computer_choice == 's' and user_input == 'p':
        print('You lose!')
    # if the user chooses anything else then write 'Invalid input' to the console
    else:
        print('Invalid input')