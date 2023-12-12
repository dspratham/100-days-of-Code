from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.
clear()
print(logo)

bidding_finished= False

bids = {}

print("Welcome to the secret auction program")
def highest_bidder(bidding_record):
    highest_bid= 0
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid= bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        
  
while not bidding_finished:
    name= input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any more bidders? Type Yes or No: ")
    if should_continue == "No":
        bidding_finished = True
    elif should_continue == "Yes":
        clear()
        
highest_bidder(bids)
