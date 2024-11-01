import random
from art_blackjack import logo 

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen = random.choice(cards) 
    return chosen


def calculate_total(user_cards):
    total = sum(user_cards)
    if (total == 21) and (len(user_cards) == 2):
        return 0
    elif total > 21 and (len(user_cards) == 2):
        user_cards.remove(11)
        user_cards.append(1)
    else:
        return total
    

def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if player_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lost!"
    elif player_score == 0:
        return "You win!"
    elif player_score > 21:
        return "You lost!"
    elif computer_score > 21:
        return "You win!"
    elif computer_score > player_score:
        return "Computer wins!"
    else:
        return "You won!"



def start_game():
    print(logo)
    player = []
    computer = []
    is_game_over = False
    
    for _ in range(2):
        player.append(deal_cards())
        computer.append(deal_cards())

    print(f"{player[0]} + {player[1]}")
    print(f"{computer[0]} + ?")


    while not is_game_over:
        player_score = calculate_total(player)
        computer_score = calculate_total(computer)
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")
        if (computer_score) == 0 or (player_score == 0) or player_score >= 21:
            is_game_over = True
        else:
            withdraw_card = input("Want to draw another card. If 'y' for yes, 'n' for no: ")
            if withdraw_card == 'y':
                player.append(deal_cards())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        print(f"Your final hand: {player}, final score: {player_score}")
        computer.append(deal_cards())
        computer_score = calculate_total(computer)
    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(player_score, computer_score))

start_game()