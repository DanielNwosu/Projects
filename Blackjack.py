import random


# Deals a card. Values range from 1 to 10
def deal_card(card_deck):
    # create a logic with which you can draw a card from the card deck
    card = random.choice(card_deck)
    # you draw one card from card_deck and assign it to card_val
    # convert values such as "Ace", "Jack", "Queen", and "King" to corresponding values
    if card[0] == "Ace":
        card_val = 1
    elif card[0] == "Jack":
        card_val = 10
    elif card[0] == "King":
        card_val = 10
    elif card[0] == "Queen":
        card_val = 10
    else:
        card_val = int(card[0])
    # remove the drawn from card_deck
    card_deck.remove(card)
    # return three things. Card is the card just drawn (e.g., ["Ace", "Hearts"])
    # card_val is its numeric value.
    return card_deck, card, card_val


# Handles the player's turn.  Returns the point value for the player's hand.
def get_score(card_deck, scores):
    score_of_player = 0
    score_of_dealer = 0
    cards_on_hand = list()
    # First draw for the player
    # Get the player's carddeck, card, and score.
    # Update player's score and cards on hand
    card_deck, card, hand_val = deal_card(card_deck)
    score_of_player += hand_val
    cards_on_hand.append(card)
    scores['player']['score'] = score_of_player
    scores['player']['cards'] += card
    # First draw for the dealer
    # Get the dealer's carddeck, card, and score.
    # Update dealer's score and cards on hand
    # Second draw for the player
    # Get the player's carddeck, card, and score.
    # Update player's score and cards on hand
    card_deck, card, hand_val = deal_card(card_deck)
    score_of_dealer += hand_val
    scores['dealer']['score'] = score_of_dealer
    scores['dealer']['cards'] += card
    # Second draw for the player
    card_deck, card, hand_val = deal_card(card_deck)
    score_of_player += hand_val
    cards_on_hand.append(card)
    scores['player']['score'] = score_of_player
    scores['player']['cards'] += card
    # Get the dealer's carddeck, card, and score.
    # Update dealer's score and cards on hand
    card_deck, card, hand_val = deal_card(card_deck)
    score_of_dealer += hand_val
    scores['dealer']['score'] = score_of_dealer
    scores['dealer']['cards'] += card
    # Show cards on player's hand
    type_of_role = 'player'
    show_cards(cards_on_hand, type_of_role)
    print("The sum of the first two cards is:", score_of_player)
    user_response = input("Do you want to take another card?: (Y/N)")
    # you should display the sum of the two cards
    # then, ask users whether they want to get another card
    # if either the user is busted or the user wants to stop, then you need to stop
    while user_response == "Y" or user_response == "y":
        # Get the player's carddeck, card, and score.
        card_deck, card, hand_val = deal_card(card_deck)
        score_of_player += hand_val
        cards_on_hand.append(card)
        scores['player']['score'] = score_of_player
        scores['player']['cards'] += card
        # update card deck, score, and drawn cards accordingly
        if score_of_player > score_of_dealer and score_of_player > 21:
            print("Your sum is now ", score_of_player, " dealer score was ", score_of_dealer, " you busted!")
            break
        else:
            print("You have", cards_on_hand)
            print("Your sum is now ", score_of_player)
            user_response = input("Do you want to take another card?: (Y/N)")
    while user_response == "N" or user_response == "n":
        if score_of_player > score_of_dealer:
            print("You have", cards_on_hand)
            print("Congrats you win!", " your score:", score_of_player, " dealer score:", score_of_dealer)
            print("dealer had", scores['dealer']['cards'])
            break
        elif score_of_player < score_of_dealer:
            print("Sorry you lose!", " your score:", score_of_player, " dealer score:", score_of_dealer)
            break
        elif score_of_player ==score_of_dealer:
            print("wow it's a draw!")
            break
        # Once you got the player_score, you have to check whether the player got busted
        # According to the result you should display different prompts.
        # ask user whether he/she wants to take another card
        user_response = input("Do you want to take another card?: (Y/N)")
    # return the player's score
    return scores


# Get two arguments (cards on hand, type of role (e.g., player, dealer))
# Display all cards on hands
def show_cards(cards, who):
    if who == 'player':
        print("You have", cards)
    # complete this part
    # Create a card deck from an input file (cards.txt).
    # Then, return 52 cards saved in a list of lists


def set_card_deck():
    # Complete this function
    file = '/home/dnnwosu525/PycharmProjects/Excercises/cards.txt'

    cards = list()
    in_file = open(file, 'r')
    for line in in_file:
        cards.append(line.rstrip().split(","))

    in_file.close()

    return cards


# The main function.  It repeatedly plays games of blackjack until the user decides to stop.

def main():
    # Prime the loop and start the first game.
    user_response = "Y"
    while user_response == "Y" or user_response == "y":
        # Set a card deck
        cards = set_card_deck()
        # Set a dictionary to manage scores of the player and dealer
        scores = {"player": {"score": 0, "cards": []}, "dealer": {"score": 0, "cards": []}}
        # Get the scores.
        scores = get_score(cards, scores)
        player_score = scores["player"]["score"]
        # Once you got the player_score, you have to check whether the player got busted, whether player's score
        # is larger than the dealer's score. According to the result you should display different prompts.
        # ask user whether he/she wants to play another game
        user_response = input("Do you want to play another game?: (Y/N)")


# Call the main function to start the blackjack program.
main()
