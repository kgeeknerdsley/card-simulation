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
        #print(player_list[i])
        #print()

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
                if(move_choice == 0):
                    to_discard = player.get(face_index[0]) #this card is now gone
                    discard_pile.add(to_discard)
                    player.add(deck.deal(2)) #draw two
                    print("Player",player_num,"discarded a face and drew two")
                else:
                    #check if players can be stolen from
                    #can't steal if hand is less than STEAL_MIN
                    #if so, choose a random player to steal from
                    print("Player",player_num,"Going to steal")


            player_num += 1

        print("Deck now has",deck.size,"cards left")

    #calculate scores and find winner



game(NUM_PLAYERS)