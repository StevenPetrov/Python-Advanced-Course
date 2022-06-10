import time
import random
from io import open
from random import randint

players_dict = dict()


def welcome():
    print('''Hi there!
This is the Liar's Dice game.
    ''')
    print('Loading...\n')
    time.sleep(1)


def players_input():
    while True:
        try:
            players = int(input('How many players do you want to play with?: '))
            break
            # TODO input 0 value exc
        except ValueError:
            print("Oh, no! You've just typed a wrong number! Please try again with 1-9: ")
    return players


def generating_players_dict(players):
    count = 0
    print('Throwing dices...\n')
    for player in range(players):
        count += 1
        player_name = f'{"Player " + str(count)}'
        players_dict[player_name] = [0, 0, 0, 0, 0]


def throwing_dices(players_dict):
    for key, value in players_dict.items():
        players_dices = len(value)
        players_dict[key] = []
        for dices in range(players_dices):
            number = randint(1, 6)
            players_dict[key].append(number)


def bot_bidding_logic(player_number, number, times, players_dict, current_bid_by):
    time.sleep(3)
    player = 'Player ' + str(player_number)
    risk_level = 0
    risk_bid = 0
    for key, values in players_dict.items():
        risk_level += len(players_dict[key])
        risk_bid += len(players_dict[key])
    risk_level *= 6
    risk_level *= times
    risk_bid *= number
    risk_bid *= times
    if risk_level * 0.7 > risk_bid and number in players_dict[player]:
        bigger_number = max(players_dict[player])
        if bigger_number > number:
            number_count = players_dict[player].count(bigger_number)
            if number_count > 0:
                random_number_gen = randint(2, 5)
                final_bid = int(number_count * 0.5 * random_number_gen)
                if final_bid < 1:
                    final_bid = 1
                print(f'Woah! {player} just outbid {current_bid_by}! He said that number {bigger_number} rolled {final_bid} times\n')
                return player, bigger_number, final_bid
            else:
                return player
        else:
            return player
    elif risk_level > risk_bid:
        random_number = randint(1, 50)
        if random_number < 20:
            return player, player
        else:
            return player
    else:
        return player


welcome()
players = (players_input())
generating_players_dict(players)

while True:
    player_number = 1
    throwing_dices(players_dict)
    print(players_dict['Player 1'])
    is_lying = False
    is_bid = False
    print('Guess how many times a random dice face was rolled:')
    number = int(input('Which number?: '))
    times = int(input('How many times?: '))
    print(f'OK! So you bet that number {number} was rolled {times} times')
    current_bid_by = 'Player 1'
    opposite = ''
    time.sleep(1)
    print('Does anyone have any higher bets?')
    for player in range(len(players_dict) - 1):
        player_number += 1
        guess = bot_bidding_logic(player_number, number, times, players_dict,current_bid_by)
        if guess:
            if len(guess) == 3:
                current_bid_by, number, times = guess
                is_bid = True
            elif len(guess) == 2:
                if is_lying:
                    print(f'{player} passed!\n')
                else:
                    player, _ = guess
                    is_lying = True
                    opposite = player
                    print(f'{player} thinks {current_bid_by} is lying!!\n')
            else:
                player = guess
                print(f'{player} passed!\n')
    if not is_lying and not is_bid:
        pass
    elif is_bid:
        print(f'Do you think {current_bid_by} is lying?')
        lies = input('yes/no: ').lower()
        # TODO exc for wrong input
        if lies == 'yes':
            opposite = 'Player 1'

    print('Revealing the dices!')
    time.sleep(2)
    for key, value in players_dict.items():
        print(f'{key}: {value}')

    while True:
        checking = times
        for key, value in players_dict.items():
            for num in value:
                if num == number:
                    checking -= 1
        if checking <= 0:
            if opposite:
                print(f'Oh, no! {opposite} just lost a dice.')
                players_dict[opposite].pop()
                break
            else:
                print("Well, it's all good for now, let's continue the game :)")
                break
        else:
            print(f'Oh, no! {current_bid_by} just lost a dice.')
            players_dict[current_bid_by].pop()
            break

    for key, value in players_dict.items():
        if len(players_dict[key]) == 0:
            removed = key
            print(f'{removed} has been eliminated!\n')
            players_dict.pop(key)
            break
    if len(players_dict) == 1:
        for winner in players_dict.keys():
            print(f'The winner is {winner}!')
            break
