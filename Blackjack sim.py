# Balck Jack Sim. Gambler Perspective
# Step 1: Create dealing system
# Step 2: Create Hit and Stand system
# Step 3: Create Payout System
import random

og_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
deck = []
player_hand = []
dealer_hand = []
stand = False
bust = False
choice = ""
bank = 5000.00
play = True
game = ""
loop = 0

def total(hand):
    total = 0
    for i in hand:
        total += i
    if total > 21 and (11 in hand):
        hand.remove(11)
        hand.append(1)
        total -= 10
    return total


while play == True:

    # Place Bet
    print("You have $", bank) 
    bet = float(input("How much are you betting?\n"))

    # Deal Hands
    deck = og_deck
    random.shuffle(deck)
    player_hand.append(deck[0])
    deck.pop(0)
    dealer_hand.append(deck[0])
    deck.pop(0)
    player_hand.append(deck[0])
    deck.pop(0)
    dealer_hand.append(deck[0])
    deck.pop(0)
    print("Player Hand: ", player_hand)
    print("Dealer Hand: ", dealer_hand[0])

    # Player Plays
    if total(player_hand) == 21:
        print("BlackJack!")
        bust = True
        bank += bet*1.5

    while (stand == False) and (bust == False):
        if loop == 0:
            #choice = input("Hit, Stand, or Double\n")
            # AI Gambler
            if total(player_hand) < 11:
                choice = "hit"
            elif total(player_hand) == 11:
                choice = "double"
            elif total(player_hand) == 10 and dealer_hand[0] <= 10:
                choice = "double"
            elif total(player_hand) == 8 and dealer_hand[0] == (5 or 6):
                choice = "double"
            elif total(player_hand) <= 15 and dealer_hand[0] != 10: 
                choice = "hit"
            elif total(player_hand) == 12 and dealer_hand[0] == (2 or 3):
                choice = "hit"
            elif player_hand == [9, 9] and dealer_hand[0] == 7:
                choice == "stand"
            else:
                choice = "stand"
            # End of AI Gambler
        else:
            #choice = input("Hit or Stand,\n")
            # AI Gambler
            if total(player_hand) <= 11:
                choice = "hit"
            elif total(player_hand) == 16 and dealer_hand[0] == 10:
                choice = "stand"
            elif total(player_hand) == 12 and dealer_hand[0] >= 9:
                choice = "hit"
            else:
                choice = "stand"
            # End of AI Gambler
        if choice.upper() == "HIT":
            loop += 1
            player_hand.append(deck[0])
            deck.pop(0)
            print(player_hand)
            print(total(player_hand))
            if total(player_hand) > 21:
                bust = True
                print("OH NO! You Busted")
                bank -= bet
        elif choice.upper() == "STAND":
            stand = True
        elif choice.upper() == "DOUBLE" and loop == 0:
            bet += bet
            player_hand.append(deck[0])
            deck.pop(0)
            print(player_hand)
            print(total(player_hand))
            if total(player_hand) > 21:
                bust = True
                print("OH NO! You Busted")
                bank -= bet
            stand = True


    # House Plays
    if bust == False:
        print("Dealer Hand: ", dealer_hand)
        while total(dealer_hand) < 17:
            dealer_hand.append(deck[0])
            deck.pop(0)
            print("Dealer Hand: ", dealer_hand)

        if total(dealer_hand) > 21:
            print("You Win!")
            bank += bet
        elif total(dealer_hand) > total(player_hand):
            print("OH NO! You Lost")
            bank -= bet
        elif total(dealer_hand) < total(player_hand):
            print("You Win!")
            bank += bet
        elif total(dealer_hand) == total(player_hand):
            print("Push")

    print("Your Bank is: $", bank)
    game = input("Would You like to play again? Yes or No\n")
    if game.upper() == "YES":
        play = True
        player_hand = []
        dealer_hand = []
        stand = False
        bust = False
        choice = ""
        loop = 0
    if game.upper() == "NO":
        play = False

print("\n\nThank you for Playing!\n\nYou Made it out with $", bank)
