import random

def play_roulette(starting_money, starting_bet, num_bets):
    money = starting_money
    bet = starting_bet

    for _ in range(num_bets):
        # Choose a color randomly with equal probability for red and black
        chosen_color = random.choices(['red', 'black'], weights=[0.4736, 0.4736])[0]

        # Check if the chosen color matches the bet
        if chosen_color == 'red':
            money += bet
            print(f'Win! Bet on red. Money: {money}')
            # Switch to black for the next bet
            chosen_color = 'black'
            bet = starting_bet
        else:
            money -= bet
            print(f'Loss. Bet on black. Money: {money}')
            # Double the bet for the next round
            bet *= 2

        # Check if the player is out of money
        if money <= 0:
            print("Out of money. Game over.")
            break

    print(f"Final money: {money}")

# variables
starting_money = int(input("Select the starting amount: "))
starting_bet = int(input("Select the starting bet: "))
num_bets = int(input("Select the number of bets: "))

play_roulette(starting_money, starting_bet, num_bets)
