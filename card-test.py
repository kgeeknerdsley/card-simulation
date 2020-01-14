import pydealer
import random
import sys

#deal each player four cards
#player can choose:
    #draw one card (neutral move)
    #discard face card, draw two cards
    #give face card to other player, steal two cards
#run for 4 complete rounds

#Simulation Parameters
NUM_PLAYERS = 4 #number of players in game
FACE_PENALTY = -10 #how many points to subtract per remaining face card
STARTING_CARDS = 4 #how many cards dealt at beginning
ROUND_NUM = 4 #how many rounds to play
STEAL_MIN = 2 #minimum cards
CARDS_TO_STEAL = 2

face_cards = ["Jack","Queen","King","Ace"]
discard_pile = pydealer.Stack()

def game(players):
    print("Game started")

    #on new game, create list with blank hands equal to number of players
    player_list = []

    # create the deck and shuffle it
    deck = pydealer.Deck()
    deck.shuffle()

    for i in range(players):
        player_list.append(pydealer.Stack) #create the player's hand
        player_list[i] = deck.deal(STARTING_CARDS) #add four cards to it

    #four game rounds
    for rounds in range(ROUND_NUM):
        print("---------------Round", rounds+1,"----------------")
        player_num = 1
        for player in player_list:
            #this is where decision logic happens

            #if the hand is entirely face cards, all you can do is draw one card
            if(not(player.find_list(face_cards))):
                player.add(deck.deal(1))
                print("Player" , player_num, "Drew one card")
            else:
                move_choice = random.randint(0,1)
                face_index = player.find_list(face_cards) #find list of face cards in hand

                #getting a card removes it from the deck! like holding it in hand
                if(move_choice == 0): #drawing two move
                    to_discard = player.get(face_index[0]) #this card is now gone
                    discard_pile.add(to_discard)
                    player.add(deck.deal(2)) #draw two
                    print("Player",player_num,"discarded a face and drew two")
                else: #stealing move
                    #check if players can be stolen from
                    safe_steals = []
                    for examine_player in player_list:
                        if(examine_player.size >= STEAL_MIN):
                            safe_steals.append(examine_player) #add the safe steal to the list



                    to_steal = random.randint(0,len(safe_steals)-1) #randomly choose a player to steal from
                    stolen_player = safe_steals[to_steal]

                    card_one = random.randint(0,stolen_player.size - 1)
                    player.add(stolen_player.get(card_one)) #take a card from stolen player and add to stealing player

                    card_two = random.randint(0, stolen_player.size - 1) #run a second time, but with new size of hand
                    player.add(stolen_player.get(card_one))

                    #can't steal if hand is less than STEAL_MIN
                    #if so, choose a random player to steal from
                    print("Player",player_num,"discarded a face and stole two cards")


            player_num += 1

        print("Deck now has",deck.size,"cards left")

    #calculate scores and find winner



game(NUM_PLAYERS)