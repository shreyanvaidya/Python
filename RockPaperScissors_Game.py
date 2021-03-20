import random

while True:
    best_of = int(input("Enter the times you want to play"))
    draw_count = 0
    win_count = 0
    loss_count = 0

    # function to count the winner
    def winner(win_count, draw_count, loss_count):
        if win_count == loss_count:
            return "\nGame is drawn"
        elif win_count > draw_count and win_count > loss_count:
            return "\nPlayer wins"
        elif draw_count > win_count and draw_count > loss_count:
            return "\nGame is drawn"
        else:
            return "\nComputer wins"


    if best_of % 2 == 0:
        print("\nenter an odd number")
        continue
    elif best_of % 2 != 0 and best_of > 2:
        game_round = 1
        while game_round <= best_of:
            user_choice = int(input('\nenter your choice\n1. for rock\n2. for paper\n3. for scissors \n'))
            choice_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
            winning_list = [(3, 2), (1, 3), (2, 1)]
            list1 = [1, 2, 3]
            computer_choice = random.choice(list1)
            if user_choice not in list1:
                print('enter valid number!!!\n 1,2 or 3')
                continue
            print('\ncomputer choice is ' + str(choice_dict[computer_choice]))
            print('\nplayer choice is ' + str(choice_dict[user_choice]))
            if user_choice == computer_choice:
                draw_count += 1
                print('\nGame is draw for round: ' + str(game_round))
            elif (user_choice, computer_choice) in winning_list:
                win_count += 1
                print('\nplayer wins for round: ' + str(game_round))
            else:
                loss_count += 1
                print('\ncomputer wins for round: ' + str(game_round))
            game_round += 1
    else:
        print("\nenter a valid choice")
        continue
    print("player won= " + str(win_count) + "\ncomputer won= " + str(loss_count) + "\ndrawn= " + str(draw_count))
    print(winner(win_count, draw_count, loss_count))
    play_again = input('\ndo you want to play again? \n(y/n)\n')
    if play_again.lower() != 'y':
        print('\nthank you for playing!')
        break
