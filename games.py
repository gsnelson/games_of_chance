import random

money = 100

card_deck = [[2, "2_clubs"], [2, "2_diamonds"], [2, "2_hearts"], [2, "2_spades"], [3, "3_clubs"], [3, "3_diamonds"], [3, "3_hearts"], [3, "3_spades"], [4, "4_clubs"], [4, "4_diamonds"], [4, "4_hearts"], [4, "4_spades"], [5, "5_clubs"], [5, "5_diamonds"], [5, "5_hearts"], [5, "5_spades"], [6, "6_clubs"], [6, "6_diamonds"], [6, "6_hearts"], [6, "6_spades"], [7, "7_clubs"], [7, "7_diamonds"], [7, "7_hearts"], [7, "7_spades"], [8, "8_clubs"], [8, "8_diamonds"], [8, "8_hearts"], [8, "8_spades"], [9, "9_clubs"], [9, "9_diamonds"], [9, "9_hearts"], [9, "9_spades"], [10, "10_clubs"], [10, "10_diamonds"], [10, "10_hearts"], [10, "10_spades"], [11, "jack_clubs"], [11, "jack_diamonds"], [11, "jack_hearts"], [11, "jack_spades"], [12, "queen_clubs"], [12, "queen_diamonds"], [12, "queen_hearts"], [12, "queen_spades"], [13, "king_clubs"], [13, "king_diamonds"], [13, "king_hearts"], [13, "king_spades"], [14, "ace_clubs"], [14, "ace_diamonds"], [14, "ace_hearts"], [14, "ace_spades"]]

#Write your game of chance functions here
def coin_flip(call, bet):
  # heads = 1, tails = 2
  flip_result = random.randint(1, 2)
  if flip_result == 1:
    print("The coin flip came up heads!")
    if call == "Heads":
      return "You win $" + str(bet) + "!"
    else:
      return "You lose $" + str(bet) + "!"
  else:
    print("The coin flip came up tails!")
    if call == "Tails":
      return "You win $" + str(bet) + "!"
    else:
      return "You lose $" + str(bet) + "!"

def chohan(call, bet):
  die1_result = random.randint(1, 6)
  print("The first die rolled a " + str(die1_result) + "!")
  die2_result = random.randint(1, 6)
  print("The second die rolled a " + str(die2_result) + "!")
  if (die1_result + die2_result) % 2 == 0:
    print("The dice total is even!")
    if call == "Even":
      return "You win $" + str(bet) + "!"
    else:
      return "You lose $" + str(bet) + "!"
  else:
    print("The dice total is odd!")
    if call == "Odd":
      return "You win $" + str(bet) + "!"
    else:
      return "You lose $" + str(bet) + "!"

def card_pick(bet):
  random.shuffle(card_deck)
  player_card = random.choice(card_deck)
  pcard_index = card_deck.index(player_card)
  print("The player card is " + player_card[1])
  del(card_deck[pcard_index])
  house_card = random.choice(card_deck)
  hcard_index = card_deck.index(house_card)
  print("The house card is " + house_card[1])
  if player_card[0] > house_card[0]:
    return "You have the higher card. You win $" + str(bet) + "!"
  elif house_card[0] > player_card[0]:
    return "The house has the higher card. You lose $" + str(bet) + "!"
  else:
    return "You and the house have the same card. This results in a push."
#Call your game of chance functions here
#print(coin_flip("Heads", 25))
#print(chohan("Odd", 15))
print(card_pick(5))