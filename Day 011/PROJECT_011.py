import random

def get_shuffled_card_set():
    cards_set = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    all_cards = []
    for index in range(0,4):
        all_cards += cards_set
    random.shuffle(all_cards)
    return all_cards

def get_card_value(card):
    if card == 'J' or card == 'Q' or card == 'K':
        return [10]
    elif card == 'A':
        return [1, 11]        
    else:
        return [card]

def get_score(cards):
    score = [0, 0, 0]
    first_ace = True
    for card in cards:
        value = get_card_value(card)
        if len(value) == 1:
            score[0] += value[0]
            score[1] += value[0]
            score[2] += value[0]
        elif len(value) == 2:
            if first_ace:
                score[0] += value[0]
                score[1] += value[0]
                score[2] += value[1]
            else:
                score[0] += value[0]
                score[1] += value[1]
                score[2] += value[1]                
    if score[0] == score[1] == score[2]:
        return [score[0]]
    if score[0] == score[1] != score[2]:
        return [score[0], score[2]]
    return score

def print_current_scores(player_cards, player_score, computer_cards, computer_score):
    if len(player_score) == 1:
        print(f"Your cards are: {player_cards}, so your current score is {player_score[0]}.")
    elif len(player_score) == 2:
        print(f"Your cards are: {player_cards}, so your current score is either {player_score[0]} or {player_score[1]}.")
    else:
        print(f"Your cards are: {player_cards}, so your current score is either {player_score[0]}, {player_score[1]} or {player_score[2]}.")
    if len(computer_cards) == 2:
        print(f"The second computer card is {computer_cards[1]}.")
    if len(computer_cards) == 3:
        print(f"The second and third computer cards are {computer_cards[1]} and {computer_cards[2]}.")
    if len(computer_cards) == 4:
        print(f"The second, third and fourth computer cards are {computer_cards[1]}, {computer_cards[2]} and {computer_cards[3]}.")

def get_best_score(scores):
    best_score = scores[0]
    for score in scores:
        if score == 21:
            return 21
        if score < 21 and 21 - score < 21 - best_score:
            best_score = score
    return best_score

def get_situation(player_score, computer_score, continue_playing):
    player_best_score = get_best_score(player_score)
    computer_best_score = get_best_score(computer_score)
    if player_best_score == 21:
        return 'win'
    if player_best_score > 21:
        return 'lose'
    if computer_best_score > 21:
        return 'win'      
    if computer_best_score == 21:
        return 'lose'           
    if player_best_score == computer_best_score and not continue_playing:
        return 'draw'
    if 21 - player_best_score < 21 - computer_best_score and not continue_playing:
        return 'win'
    if 21 - player_best_score > 21 - computer_best_score and not continue_playing:
        return 'lose'    
    return 'continue'

def print_results(result, player_cards, computer_cards):
    print(f"Your cards: {player_cards}.")
    print(f"Computer cards: {computer_cards}.")
    if result == 'win':
        print("YOU WIN !!!\n")
    elif result == 'lose':
        print("YOU LOSE !!!\n")
    elif result == 'draw':
        print("IT'S A DRAW !!!\n")


player_score = get_score(['A', 3, 'K'])
computer_score = get_score(['A', 2, 10])
situation = get_situation(player_score, computer_score, not False)
print(situation)
first_game = True

while True:
    if first_game:
        play = input("\n*********************************\n\nDo you want to play blackjack (y or no)? ")
        first_game = False
    else:
        play = input("*********************************\n\nAnother game (y or no)? ")
    if play != 'y':
        break

    card_set = get_shuffled_card_set()
    player_cards = [card_set.pop(0)]
    computer_cards = [card_set.pop(0)]
    player_cards.append(card_set.pop(0))
    computer_cards.append(card_set.pop(0))
    player_score = get_score(player_cards)
    computer_score = get_score(computer_cards)
    print_current_scores(player_cards, player_score, computer_cards, computer_score)
    player_best_score = get_best_score(player_score)
    if player_best_score == 21:
        print_results('win', player_cards, computer_cards)
        continue

    game_over = False
    draw_new_card = 'y'



    while not game_over:

        if draw_new_card != 'n':
            draw_new_card = input("Do you want to get another card (y or n)? ")
        if draw_new_card == 'y':
            player_cards.append(card_set.pop(0))
        if computer_score[0] < 17 or (len(computer_score) == 2 and computer_score[1] < 17) or (len(computer_score) == 3 and computer_score[2] < 17):
            computer_cards.append(card_set.pop(0))            
        player_score = get_score(player_cards)
        computer_score = get_score(computer_cards)
        print_current_scores(player_cards, player_score, computer_cards, computer_score)
        situation = get_situation(player_score, computer_score, not game_over)
        
        if situation == 'win' or situation == 'lose' or situation == 'draw':
            game_over = True
        for score in computer_score:
            if score >= 17 and draw_new_card == 'n':
                game_over = True
        if game_over:
            situation = get_situation(player_score, computer_score, not game_over)
            print_results(situation, player_cards, computer_cards)
