import art

print(art.logo)
print("Welcome to the secret auction program.")

bids = {}

while True:
    name = input("What is your name? ")
    bid = input("What is your bid ($)? ")
    if not bid.isdecimal():
        print("Bid must be a number!")
        continue
    bid = int(bid)
    others = input("Are there any other biddrs (y or n) ? ")
    bids[name] = bid
    if others != 'y':
        break

winner = ''
bid = 0
for key in bids:
    value = bids[key]
    if value > bid:
        winner = key
        bid = value

print(f"The winner is {winner} with a bid of ${bid}.")