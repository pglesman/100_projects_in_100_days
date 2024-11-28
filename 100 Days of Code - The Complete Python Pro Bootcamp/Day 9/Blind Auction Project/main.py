import art

print(art.logo)
auction_dict = {}

while True:
    # TODO-1: Ask the user for input
    user_name = input("Tell me your name: ")
    user_bid = int(input("Tell me your bid: $"))
    # TODO-2: Save data into dictionary {name: price}
    auction_dict[user_name] = user_bid
    # TODO-3: Whether if new bids need to be added
    auction_over = input("Are there other participants? Yes or no?").lower()
    user_bid_max = 0
    user_name_max = ''
    if auction_over == 'no':
        for key in auction_dict:
            if auction_dict[key] > user_bid_max:
                user_bid_max = auction_dict[key]
                user_name_max = key
        print(f"The highest bid goes to {user_name_max} with bid {user_bid_max}. Congratulations!")
        break
