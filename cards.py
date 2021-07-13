import random
import math

characters = [
    "Mrs. White", 
    "Mrs. Peacock", 
    "Professor Plum", 
    "Colonel Mustard", 
    "Miss Scarlett", 
    "Mr. Green", 
]

weapons = [
    "Knife", 
    "Revolver", 
    "Rope", 
    "Wrench",
    "Candlestick", 
    "Lead pipe"
]

rooms = [
    "Billiard Room", 
    "Conservatory", 
    "Dining Hall", 
    "Kitchen", 
    "Hall", 
    "Ballroom", 
    "Lounge", 
    "Library", 
    "Study"
]

the_murder = ['Mrs. Peacock', 'Hall', 'Lead pipe']
# def random_murder():
#     murderer = random.choice(characters)
#     murder_location = random.choice(rooms)
#     murder_weapon = random.choice(weapons)

#     the_murder.append(murderer)
#     the_murder.append(murder_location)
#     the_murder.append(murder_weapon)

def determine_game_size():
    number_of_players = int(input("How many players would you like to compete against? Pick a number between 2 and 5: "))
    return number_of_players

cards = []
cards.extend(characters)
cards.extend(weapons)
cards.extend(rooms)

cards.remove(the_murder[0])
cards.remove(the_murder[1])
cards.remove(the_murder[2])

random.shuffle(cards)

#This game size DOES NOT account for the player, only the number of other players
game_size = determine_game_size()

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

smaller_deck = list(split(cards, game_size + 1))
player_deck = list(smaller_deck[0])

print("\nYou're clues are:", player_deck, "\n")

other_player_numbers =[]
other_players = range(game_size)
for n in other_players:
    text = "Player {}".format(n + 1)
    other_player_numbers.append(text)
    
print(other_player_numbers)
