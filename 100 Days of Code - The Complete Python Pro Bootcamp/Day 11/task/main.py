import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    play_game = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
    if play_game == 'n':
        break

    print('\n' * 100)
    print(art.logo)

    player_cards = random.choices(cards, k=2)
    comp_cards = [random.choice(cards)]

    player_score = sum(player_cards)
    comp_score = sum(comp_cards)

    while player_score <= 21:
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {comp_cards}")

        pass_or_not = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
        if pass_or_not == 'y':
            player_new_card = random.choice(cards)
            if player_new_card == 11 and player_score + player_new_card > 21:
                player_new_card = 1
            player_cards.append(player_new_card)
            player_score += player_new_card
            continue
        elif pass_or_not == 'n':
            break

    while comp_score <= player_score and player_score <= 21 and comp_score != 21:
        comp_new_card = random.choice(cards)
        if comp_new_card == 11 and comp_score + comp_new_card > 21:
            comp_new_card = 1
        comp_cards.append(comp_new_card)
        comp_score += comp_new_card

    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    if player_score > 21:
        print("You went over. You lose.")
    elif comp_score > 21:
        print("Opponent went over. You win.")
    elif player_score < 21 and comp_score == 21:
        print("Lose, opponent has Blackjack")
    elif player_score < comp_score:
        print("You lose, opponent has better score.")
    elif player_score == comp_score:
        print("Draw.")
