import random

start = "\033[1m"
end = "\033[0;0m"

while True:
    user_action = input('Choose from rock, paper, scissors and enter your choice: ')
    user_action = user_action.lower()

    computer_choice = ['rock', 'paper', 'scissors']
    computer_action = random.choice(computer_choice)

    print(f'\nIf you choose {start}{user_action}{end} computer chooses {start}{computer_action}{end}.')

    if user_action == computer_action:
        print(f"You both choosed {user_action}. {start}It's a tie!{end}")
    elif user_action == 'rock':
        if computer_action == 'paper':
            print(f"A {computer_action} can wrap a {user_action} so {start}computer wins!{end}")
        else:
            print(f"Your {user_action} damaged the {computer_action} so {start}you win!{end}")
    elif user_action == 'paper':
        if computer_action == 'rock':
            print(f"Your {user_action} wraps the {computer_action} so {start}you win!{end}")
        else:
            print(f"These {computer_action} just cut your {user_action} so {start}you lost!{end}")
    elif user_action == 'scissors':
        if computer_action == 'rock':
            print(f"Your {user_action} were damaged by the {computer_action}. {start}Computer wins!{end}")
        else:
            print(f"Your {user_action} just cut {computer_action} into pieces and {start}you win!{end}")

    play_again = input('\nDo you want to play again? Enter yes or no: ')
    play_again = play_again.lower()
    if play_again == 'no':
        print('See you next time!')
        break