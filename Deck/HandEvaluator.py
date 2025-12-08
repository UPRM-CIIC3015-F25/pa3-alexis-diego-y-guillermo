from Cards.Card import Card, Rank, Suit

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    suitOrder = [Suit.HEARTS, Suit.CLUBS, Suit.DIAMONDS, Suit.SPADES]  # Define the order of suits
    rankOrder = [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE, Rank.TEN,
                 Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE]
    rank_dic = {}
    rank_list = []
    suit_dic = {}
    suit_list = []
    #Creates sorted list containing all suits
    for suit in suitOrder:
        for card in hand:
            if card.suit == suit:
                suit_list.append(card.suit)
    #Creates Dictionary containing the frequency of each suit
    for suit in suitOrder:
        for card in hand:
            if card.suit == suit:
                if card.suit not in suit_dic:
                    suit_dic[card.suit] = 1
                else:
                    suit_dic[card.suit] += 1
    # Creates sorted list containing all ranks
    for rank in rankOrder:
        for card in hand:
            if card.rank == rank:
                rank_list.append(card.rank)
    # Creates Dictionary containing the frequency of each rank
    for rank in rankOrder:
        for card in hand:
            if card.rank == rank:
                if card.rank not in rank_dic:
                    rank_dic[card.rank] = 1
                else:
                    rank_dic[card.rank] += 1
    #These lines check for: Straight Flush, Straight, and Flush
    straight_check_list = rankOrder[rankOrder.index(rank_list[0]):rankOrder.index(rank_list[-1])]
    straight_status = False
    for i in range(0,len(straight_check_list)):
        if rank_list[i] == straight_check_list[i]:
            straight_status = True
        else:
            straight_status = False
            break
    if straight_status == True and len(suit_dic) == 1:
        return "Straight Flush"
    elif straight_status == True:
        return "Straight"
    if len(suit_dic) == 1 and straight_status == False:
        return "Flush"
    #These lines check for full house and Two Pairs
    rank_values = sorted(rank_dic.values())
    if rank_values[0] == 2 and rank_values[1] == 3:
        return "Full House"
    elif rank_values[0] == 1 and rank_values[1] == 2 and rank_values[2] == 2:
        return "Two Pairs"
    #Checks for all remaining possible cases
    for x in rank_dic:
        if rank_dic[x] == 4:
            return "Four of a Kind"
        elif rank_dic[x] == 3:
            return "Three of a Kind"
        elif rank_dic[x] == 2:
            return "One Pair"
    return "High Card"  # If none of the above, it's High Card
