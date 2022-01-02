import random
import math


def game():
    user = input("What's your choice ? 'p' for paper, 'r' for rock, 's' for scissors \n" )
    user = user.lower()

    opponent = random.choice(['p','r','s'])

    if user == opponent:
        return (0,user,opponent)

    if is_win(user,opponent):
        return (1,user,opponent)
    return (-1,user,opponent)

def is_win(player,enemy):
 if (player == 'r' and enemy == 's') or (player == 's' and enemy == 'p') or (player == 'p' and enemy == 'r'):
    return True
 return False


def play_best_of(n):
   
    player_wins = 0
    opponent_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and opponent_wins < wins_necessary:
        result, user, opponent = game()

        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user, opponent))
        else:
            opponent_wins += 1
            print('You chose {} and the computer chose {}. You lost :(\n'.format(user, opponent))

    if player_wins > opponent_wins:
        print('You have won the best of {} games! '.format(n))
    else:
        print('You lost loser :('.format(n))

if __name__ == '__main__':
    play_best_of(5) 