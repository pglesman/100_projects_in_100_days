import random
import art
import game_data

a_comp, b_comp = random.sample(game_data.data, 2)
score = 0

while True:
    a_follow = a_comp['follower_count']
    b_follow = b_comp['follower_count']
    print(art.logo)

    if score > 0:
        print(f'You\'re right! Current score {score}.')

    print(f"Compare A: {a_comp['name']}, a {a_comp['description']}, from {a_comp["country"]}.")
    print(art.vs)
    print(f"Against B: {b_comp['name']}, a {b_comp['description']}, from {b_comp["country"]}.")
    answer = input("Who has more followers? Type \'A\' or \'B\': ").lower()

    if answer == 'a' and a_follow > b_follow or answer == 'b' and b_follow > a_follow:
        score += 1
        a_comp = b_comp
        # Create a new list just for switching new things to compare
        new_game_data = game_data.data
        # Delete from the new list the first thing to compare
        new_game_data.pop(game_data.data.index(b_comp))
        # Pick a competitor from list where there isn't a first competitor
        b_comp = random.choice(new_game_data)
        continue
    else:
        print("\n" * 100)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
