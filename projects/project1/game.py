from projects.project1.card import Card, Face, MultiDeck

class Game:
    def __init__(self):
        self.deck = MultiDeck()

    def calculate_score(self, hand):
        """ starts off score at zero, and then adds it all up. Also checks for logic of having aces 
        count as either 11 or 1 depending on the current score """
        score = 0
        num_aces = 0 
        for card in hand:
            if card.face == Face.ACE:
                num_aces += 1
                score += 11
            else:
                score += card.face.face_value()

        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1

        return score


    def show_hands(self, reveal_dealer = False):
        """ shows the score of the dealer and player, and has the dealer's score hidden initially. """
        print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} | Score: {self.calculate_score(self.player_hand)}")
        if reveal_dealer:
            print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.calculate_score(self.dealer_hand)}")
        else:
            dealer_card = [self.dealer_hand[0]]
            print(f"Dealer's Hand: {"".join(str(card) for card in dealer_card)} [Hidden] | Score: {dealer_card[0].face.face_value()}")

    def show_player(self):
        """ created to show ONLY the player's score on their turn """
        print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} | Score: {self.calculate_score(self.player_hand)}")

    def show_dealer(self):
        """ only shows the dealer's score when called """
        print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.calculate_score(self.dealer_hand)}")


    def player_turn(self):
        while True:
            self.show_player()
            choice = input("(H)it or (S)tay?").strip().upper()
            print("")
            if choice == "H":
                self.player_hand.append(self.deck.draw_card())
                if self.calculate_score(self.player_hand)>21:
                    self.show_player()
                    print("Bust! You went over 21.")
                    print("")
                    print("Final Hands:")
                    self.show_hands(reveal_dealer=True)
                    print("")
                    return False
                if self.calculate_score(self.player_hand) == 21:
                    print("Player has Blackjack! Player wins.")
                    return False
            else:
                return True
                
    def dealer_turn(self):
        self.show_dealer() # shows the fully revealed dealer score and hand
        print("")
        while self.calculate_score(self.dealer_hand) < 17: # continual drawing of cards until at least 17 is reached
            self.dealer_hand.append(self.deck.draw_card())

        if self.calculate_score(self.dealer_hand)>21:
            self.show_dealer()
            print("Dealer busts! Player wins.")
            print("")
            print("Final Hands:")
            self.show_hands(reveal_dealer=True)
            print("")
            # printed as this breaks the round
            return False
        if self.calculate_score(self.dealer_hand)==21:
            print("Dealer has Blackjack, Dealer wins!")
            return False
        return True
        
    def winner(self):
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

        print("Final Hands:")
        self.show_hands(reveal_dealer=True)
        print("")

        if player_score > dealer_score:
            print("Player Wins!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie.")

    def play_game(self):
        self.deck = MultiDeck()
        self.player_hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer_hand = [self.deck.draw_card(), self.deck.draw_card()]
        """ makes sure there is a new deck for the players each round """
        print("Initial Deal:")
        self.show_hands()
        print("")
        
        if not self.player_turn():
            return
        if not self.dealer_turn():
            return

        self.winner()

    def play(self):
        while True:
            print("Welcome to Blackjack!")
            print("")
            self.play_game()
            if input ("Would you like to play again? Y/N").strip().upper() != "Y":
                print("Game over, thanks for playing!")
                break