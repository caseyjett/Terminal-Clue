import random 

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
    "Ballroom", 
    "Billiard Room", 
    "Conservatory", 
    "Dining Hall", 
    "Kitchen", 
    "Hall", 
    "Lounge", 
    "Library", 
    "Study"
]

#THE MURDER
the_murder = []
def random_murder():
    murderer = random.choice(characters)
    murder_location = random.choice(rooms)
    murder_weapon = random.choice(weapons)

    the_murder.append(murderer)
    the_murder.append(murder_location)
    the_murder.append(murder_weapon)

# #DETERMINE NUMBER OF PLAYERS *This would be used if I can figure out a way to sort cards with a varying number of players
# def determine_game_size():
#     number_of_players = int(input("How many players would you like to compete against? Pick a number between 2 and 5: "))
#     return number_of_players

#CALLING THE ACTION
random_murder()

#BUILDING CARD DECKS
cards = []
cards.extend(characters)
cards.extend(weapons)
cards.extend(rooms)

cards.remove(the_murder[0])
cards.remove(the_murder[1])
cards.remove(the_murder[2])

random.shuffle(cards)

#SORT CARDS and assign to the 3 players
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

smaller_deck = list(split(cards, 3))

player_cards = smaller_deck[0]
computer_1 = smaller_deck[1]
computer_2 = smaller_deck[2]

# These will be the clues that the player has seen
seen_clues = []
for i in player_cards:
    seen_clues.append(i)

character_clues = []
for j in player_cards:
    if j in characters:
        character_clues.append(j)

weapon_clues = []
for k in player_cards:
    if k in weapons:
        weapon_clues.append(k)

room_clues = []
for l in player_cards:
    if l in rooms:
        room_clues.append(l)


#BEGINNING OF CLASSES
class Player: 
    def __init__(self, name, starting_room, char):
        self.name = name
        self.current_room = starting_room
        self.char = char

    def pick_player(self):
        print("\nWelcome to the Tudor Mansion. Which character would you like to play as? \n")
        for idx, character in enumerate(characters):
            print(f"---{idx}) {character}")
        chosen_character = int(input("\nEnter a number: "))
        play_as = characters[chosen_character]
        print(f"You are now {play_as} \n")
        self.char = characters[chosen_character] 
        print(f"\n**{self.char}, today there has been a murder at the Tudor Mansion and it is your job to solve it. You, Detective Gordon, and Sherlock each have six clues. Those clues tell you people that are NOT the murderer, rooms that are NOT the murder location, and items that are NOT the murder weapon. You will navigate room to room guessing what may have happened in that room. When you guess, Detective Gordon or Sherlock will share their clues if they have any. Once you have determined the murder details, you will make an accusation. You only get one chance to make an accusation so make sure that you are positive! You begin in the Billiard Room and can only move into rooms that are north, south, east or west. Rooms at the 4 corners of the mansion have secret tunnels connecting them to the room diagonal from them. You can check out the map anytime you want to. \n\nHere are your clues: {player_cards}\n")


    def next_room(self):
        current = self.current_room
        print(f"Which room would you like to go to next, {self.char}?")
        for idx, room in enumerate(current.connections):
            print(f'---{idx}) {room.name}')
        chosen_room = int(input("\nEnter a number: "))
        self.current_room = current.connections[chosen_room]
        print(f"You are now in the {self.current_room.name}.\n") 

    def guess(self):
        print("\nGuess the killer:")
        for idx, character in enumerate(characters):
            print(f"---{idx}) {character}")
        murderer_guess = int(input(" "))
        print("\nGuess the weapon:")
        for idx, weapon in enumerate(weapons):
            print(f"---{idx}) {weapon}")
        weapon_guess = int(input(" "))
        print(f"You are guessing that: {characters[murderer_guess]} killed Mr. Body with the {weapons[weapon_guess]} in the {self.current_room.name}.\n")
        guess = 0
        for i in range(len(computer_1)):
            if computer_1[i] == characters[murderer_guess] or computer_1[i] == weapons[weapon_guess] or computer_1[i] == self.current_room.name:
                # Need a way to only show one card not all of them
                print(f"Detective Gordon knows that it's not: {computer_1[i]} \n")
                seen_clues.append(f'{computer_1[i]} from Detective Gordon')
                if computer_1[i] in characters:
                    character_clues.append(computer_1[i])
                elif computer_1[i] in weapons:
                    weapon_clues.append(computer_1[i])
                elif computer_1[i] in rooms:
                    room_clues.append(computer_1[i])
                    
                guess += 1
                break
        if guess < 1: 
            for i in range(len(computer_1)):
                if computer_2[i] == characters[murderer_guess] or computer_2[i] == weapons[weapon_guess] or computer_2[i] == self.current_room.name:
                    # Need a way to only show one card not all of them
                    print(f"Sherlock knows that it's not: {computer_2[i]} \n")
                    seen_clues.append(f'{computer_2[i]} from Sherlock')
                    if computer_2[i] in characters:
                        character_clues.append(computer_2[i])
                    elif computer_2[i] in weapons:
                        weapon_clues.append(computer_2[i])
                    elif computer_2[i] in rooms:
                        room_clues.append(computer_2[i])
                    guess += 1
                    break

        if guess == 0: 
            print("Detective Gordon and Sherlock don't have any clues to share.\n")
    
            

    def accusation(self):
        warning = input("Warning: An accusation will end the game. Are you confident enough to proceed? Y/N  ")
        if warning.upper() == 'Y':
            print("\n")
            for idx, character in enumerate(characters):
                print(f"---{idx}) {character}")
            murderer_accusation = int(input("Enter the number corresponding with the murderer: "))
            print("\n")
            for idx, weapon in enumerate(weapons):
                print(f"---{idx}) {weapon}")
            weapon_accusation = int(input("Enter the number corresponding with the murder weapon: "))
            print("\n")
            for idx, room in enumerate(rooms):
                print(f"---{idx}) {room}")
            room_accusation = int(input("Enter the number corresponding with the room where the murder took place: "))
            print("\n")
            #Print characters, weapons, and rooms
            print(f"--You believe that {characters[murderer_accusation]} used the {weapons[weapon_accusation]} in the {rooms[room_accusation]}!!--")
            final_accusation = input("Is this your final accusation? Y/N  ").upper()
            if final_accusation == "Y":
                if the_murder[0] == characters[murderer_accusation] and the_murder[1] == rooms[room_accusation] and the_murder[2] == weapons[weapon_accusation]:
                    print(f"\nCongratulation {self.char} you have solved Mr. Body's murder!!!\n\n")
                else:
                    print(f"\nToday you failed Mr. Body. Here is what actaully happened: {the_murder[0]} killed Mr. Body in the {the_murder[1]} with the {the_murder[2]}.\n\n")
            elif final_accusation == "N":
                self.accusation()
            else:
                print("That was not a valid response. Try again\n")
                self.accusation()
        else: 
            #Exit the accusation
            pass

class Room:

    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_adjacent_room(self, room):
        self.connections.append(room)


#MAIN GAME PLAY
def in_play():
    ballroom = Room("Ballroom")
    billiard_room = Room("Billiard Room")
    conservatory = Room("Conservatory")
    dining_hall = Room("Dining Hall")
    kitchen = Room("Kitchen")
    hall = Room("Hall")
    lounge = Room("Lounge")
    library = Room("Library")
    study = Room("Study")

    ballroom.add_adjacent_room(conservatory)
    ballroom.add_adjacent_room(billiard_room)
    ballroom.add_adjacent_room(kitchen)

    billiard_room.add_adjacent_room(ballroom)
    billiard_room.add_adjacent_room(dining_hall)
    billiard_room.add_adjacent_room(library)
    billiard_room.add_adjacent_room(hall)

    conservatory.add_adjacent_room(library)
    conservatory.add_adjacent_room(ballroom)
    conservatory.add_adjacent_room(lounge)

    dining_hall.add_adjacent_room(lounge)
    dining_hall.add_adjacent_room(kitchen)
    dining_hall.add_adjacent_room(billiard_room)

    kitchen.add_adjacent_room(ballroom)
    kitchen.add_adjacent_room(dining_hall)
    kitchen.add_adjacent_room(study)

    hall.add_adjacent_room(study)
    hall.add_adjacent_room(lounge)
    hall.add_adjacent_room(billiard_room)

    lounge.add_adjacent_room(conservatory)
    lounge.add_adjacent_room(hall)
    lounge.add_adjacent_room(dining_hall)

    library.add_adjacent_room(study)
    library.add_adjacent_room(billiard_room)
    library.add_adjacent_room(conservatory)

    study.add_adjacent_room(library)
    study.add_adjacent_room(hall)
    study.add_adjacent_room(kitchen)


    # Start of Game
    player = Player("player", billiard_room, "Player")
    player.pick_player()


    while True:
        print(player.char, ", what would you like to do? Type:")
        print("---'G' to make a guess \n---'S' to switch rooms \n---'M' to see the map \n---'C' to see your clues \n---'P' to see possible murder details\n---'A' to make the final accusation \n---'Q' to Quit.")
        choice = input(" ").upper()
        if choice == "G":
            player.guess()
        elif choice == "S":
            player.next_room()
        elif choice == "M":
            print(f"""
            You are currently in the {player.current_room.name}
                    X--------------------------------------------X
                    |              |              |              |
                    |    Study     |    Hall      |   Lounge     |
                    |              |              |              |
                    |--------------------------------------------|
                    |              |              |              |
                    |              |              |              |
                    |   Library    |   Billiard   |    Dining    |
                    |              |     Room     |     Hall     |
                    |              |              |              |  
                    |--------------------------------------------|
                    |              |              |              |
                    | Conservatory |   Ballroom   |    Kitchen   |
                    |              |              |              |
                    X--------------------------------------------X
                    """)
        elif choice == 'C':
            print(f'\nHere are the clues you have seen so far: \n-- Charactars: {character_clues}\n-- Weapons: {weapon_clues}\n-- Rooms: {room_clues}\n')
        elif choice == "P":
            print(f"Here are all of the possibilities: \n--Characters: {characters} \n--Weapons: {weapons} \n--Rooms: {rooms}\n")
        elif choice == "A":
            player.accusation()
            break
        elif choice == "Q":
            break
        else:
            continue




in_play()





    

