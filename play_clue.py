import random

characters = [
    "Mrs. White", 
    "Mrs. Peacock", 
    "Professor Plum", 
    "Colonel Mustard", 
    "Miss Scarlett", 
    "Mr. Green", 
]

rooms = [
    "Ball Room", 
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
weapons = [
    "Knife", 
    "Revolver", 
    "Rope", 
    "Wrench"
    "Candlestick", 
    "Lead pipe"
]

def pick_character():
    player = input("Which character would you like to play as?  ")
    print("\n")

    if player not in characters:
        print("You need to pick a character from the game. You can choose from: ")
        for chars in characters:
            print("  -------  " + chars)
        print("\n")

    # if player in characters: 
    # Figure out a way to remove that name from the list for characters to ask 

def pick_starting_room():
    room_assignment = input("Which room would you like to start the game in?   ") 
    print("\n") 

    if room_assignment not in rooms: 
        print("You need to pick a room on the gameboard. You can choose from: ")
        for room in rooms:
            print("  -------  " + room)
        print("\n")

the_murder = []
def random_murder():
    random_character = random.randint(0, len(characters) -1)
    murderer = characters[random_character]

    random_room = random.randint(0, len(rooms) -1)
    murder_location = rooms[random_room]

    random_weapon = random.randint(0, len(weapons) -1)
    murder_weapon = weapons[random_weapon]

    the_murder.append(murderer)
    the_murder.append(murder_location)
    the_murder.append(murder_weapon)


pick_character()
pick_starting_room()
random_murder()
print(the_murder)