from replit import clear

print("Welcome to the Secret Auction Program")
offers = {}
user_name = input("What is your name?\n")
user_bid = int(input("What is your bid?\n$"))

other_biders = input('Are there any others bidders? Type "yes" or "no"\n')
offers[user_name] = user_bid
clear()

while other_biders == "yes":
    user_name = input("What is your name?\n")
    user_bid = int(input("What is your bid?\n$"))

    other_biders = input('Are there any others bidders? Type "yes" or "no"\n')

    offers[user_name] = user_bid
    clear()

if other_biders == "no":
    values_offers = offers.values()
    max_auction = max(values_offers)

    for name in offers:
        if offers[name] == max_auction:
            print(f"The winner is {name} with a bid of ${max_auction}.")


# Other way for find max offert with for loop
"""max_offert = 0
for name in offers:
    if offers[name] > max_offert:
        max_offert = offers[name]
print(max_offert)"""
