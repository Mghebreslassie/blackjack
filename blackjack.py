import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':10}
class Deck():
    
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)
        
    def shuffle_deck(self):
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
        
    def show_card(self):
        return f"{self.rank} of {self.suit}"

    def show_blank(self):
        return f"Face down card"
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Player():
    
    def __init__(self, name = 'Dealer', bankroll = 0):
        self.name = name
        self.bankroll = bankroll
        self.cards = []
        
    def hit(self, card):
        self.cards.append(card)
    
    def stay(self):
        print("Your turn is over")
    
    def total(self):
        card_total = 0
        for card in self.cards:
            card_total += card.value
        for card in self.cards:
            if card_total > 21:
                if card.rank == 'Ace':
                    card_total -= 10
        return card_total
    
    def win_bet(self, bet_amount):
        self.bankroll += bet_amount*2
        
    def lose_bet(self, bet_amount):
        pass
    def clear_cards(self):
        self.cards = []
        
    def tie(self,bet_amount):
        self.bankroll += bet_amount
        
    def set_bet(self, amount):
        if self.bankroll - amount >= 0:
            self.bankroll -= amount
            print(f"You bet {amount}")
        else:
            print("You don't enough to cover that bet")

def check_for_win(player, dealer, player_total, dealer_total, bet_amount):
    print(f"Player total is {player.total()}")
    print(f"Dealer total is {dealer.total()}")
    if player_total == dealer_total:
        player.tie(bet_amount)
        return "It's a draw"
    elif player_total > dealer_total:
        player.win_bet(bet_amount)
        return f"{player.name} wins"
    else:
        player.lose_bet(bet_amount)
        return "Dealer wins"


def show_cards(player, dealer):
    print(f"You have {player.cards[0].show_card()} and {player.cards[1].show_card()}")
    print(f"Dealer has {dealer.cards[0].show_card()} and {dealer.cards[1].show_blank()}")

def blackjack():
    #game logic
    
    game_on = input('Would you like to play blackjack? Type y')
    
    while game_on[0].lower() == 'y':
        name = input('What is your name?')
        money = int(input('How much money do you have?'))
        
        player = Player(name, money)
        dealer = Player()
        
        
        #round start
        playing = True
        while playing:
            deck = Deck()
            deck.shuffle_deck()
            #clear cards
            player.clear_cards()
            dealer.clear_cards()
            player_busted = False
            dealer_busted = False
            #set bet
            bet_amount = int(input('How much would you like to bet?'))
            #if else to break loop if not enough
            player.set_bet(bet_amount)
            #deal cards
            player.hit(deck.deal_card())
            player.hit(deck.deal_card())
            dealer.hit(deck.deal_card())
            dealer.hit(deck.deal_card())
            #show cards
            show_cards(player, dealer)
            
            player_total = player.total()
            dealer_total = dealer.total()
            #player turn loop?
            player_turn = True
            while player_turn:
                player_total = player.total()
                print(f"Your total is {player_total}")
                if player_total > 21:
                    print("Player busted")
                    player_busted = True
                    player_turn = False
                else:
                    hit = input("Would you like to hit or stay? type y for yes")
                    if hit[0].lower() == 'y':
                        new_card = deck.deal_card()
                        print(new_card.show_card())
                        player.hit(new_card)
                    else:
                        print('You stayed.')
                        player_turn = False
            #dealer turn loop?
            dealer_turn = True
            while dealer_turn and not player_busted:
                dealer_total = dealer.total()
                print(f"Dealer total is {dealer_total}")
                
                if dealer_total > 21:
                    print("Dealer busted.")
                    dealer_busted = True
                    dealer_turn = False
                elif dealer_total <= player_total:
                    new_card = deck.deal_card()
                    print(new_card.show_card())
                    dealer.hit(new_card)
                else:
                    dealer_turn = False
          
            if player_busted == False and dealer_busted == False:
                win_condition = check_for_win(player, dealer, player_total, dealer_total, bet_amount)
                print(win_condition)
                
            elif player_busted == True:
                player.lose_bet(bet_amount)
                print(f'{player.name} loses {bet_amount}')
            elif dealer_busted == True:
                player.win_bet(bet_amount)
                print(f'{player.name} wins {bet_amount}')
            print(f"You have {player.bankroll} in your bankroll")
            play_again = input("Would you like to play again? type y")
            if play_again[0].lower() != 'y':
                print("Game over")
                playing = False
                game_on = 'n'
                break
            #check win
            #apply bet amount
            #ask to play again

if __name__ == '__main__':
    blackjack()