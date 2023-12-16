import random
from art import logo
from replit import clear


#NEW 
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def blackjack():
  
  print(logo)
  
  is_game_over= False
  dealer_cards = []
  user_cards = []
  for i in range (2):
    dealer_cards.append(deal_card())
    user_cards.append(deal_card())
  
  def calculate_score(cards):
    """Returns the score of the user's hand"""
    if sum(cards) == 21:
      return 0
    elif 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1) 
    
    return sum(cards)
  
  def compare_scores(dealer_score, user_score):
    # dealer_score = calculate_score(dealer_cards)
    # user_score = calculate_score(user_cards)
    if dealer_score == 0:
      print("Dealer has a blackjack. You lose.")
    elif user_score == 0:
      print("You have a blackjack. You win.")
    elif user_score > 21:
      print("You bust. You lose.")
    elif dealer_score > 21:
      print("Dealer busts. You win.")
    elif dealer_score > user_score:
      print("Dealer wins.")
    elif user_score > dealer_score:
      print("You win.")
    else:
      print("It's a draw.")
  
  while not is_game_over:
      
          
    dealer_score = calculate_score(dealer_cards)
    user_score = calculate_score(user_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {dealer_cards[0]}")
    
    
    if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
          user_cards.append(deal_card())
      else:
          is_game_over = True 
  
  
  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)
    print(f" Computer's cards: {dealer_cards}, current score: {dealer_score}")
  
  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {dealer_cards}, final score: {dealer_score}")
  compare_scores(dealer_score, user_score)
  
while (input("Do you want to play a game of Blackjack?: (y/n)")) == "y":
  blackjack()
