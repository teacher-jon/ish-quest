import time
import sys

def slow_print(text, delay=0.03):
    """Prints text slowly for a retro RPG feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Player:
    def __init__(self):
        self.hp = 3
        self.inventory = []
        self.location = "Village"
        self.has_sword = False

def show_intro():
    print("\n" + "="*40)
    print("   THE LEGEND OF SUFFIXIA: THE ISH QUEST")
    print("="*40)
    slow_print("The land of Grammar is in chaos!")
    slow_print("The Evil Sorcerer 'Vaguely' has stolen all clarity.")
    slow_print("Everything is sort of... kind of... but not quite right.")
    slow_print("You, the Hero of Words, must use the ancient Suffix Sword")
    slow_print("to restore meaning to the world.\n")
    print("COMMANDS: go [north/south/east/west], look, inventory, help, quit")

def game_loop():
    player = Player()
    
    # Map structure: Keys are room names. Values are dicts with description, paths, and puzzles.
    world = {
        "Village": {
            "desc": "You are in the Village of Roots. To the North is the Forest.",
            "paths": {"north": "Misty Forest", "east": "Schoolhouse"},
            "item": "Suffix Sword (-ish)"
        },
        "Schoolhouse": {
            "desc": "An old library. There is a dusty book open to a page about Colors.",
            "paths": {"west": "Village"},
            "puzzle": {
                "question": "The walls here aren't quite red, but they are somewhat red. What are they?",
                "answer": "reddish",
                "reward": "Potion"
            }
        },
        "Misty Forest": {
            "desc": "A foggy wood. Shadows lurk here. To the North lies the Cave.",
            "paths": {"south": "Village", "north": "Cave of Confusion"},
            "enemy": {
                "name": "Giant Baby",
                "desc": "A giant baby blocks the path! He is acting very immature.",
                "weakness": "childish", # Base word: Child
                "hint": "He is acting like a child. He is..."
            }
        },
        "Cave of Confusion": {
            "desc": "Darkness surrounds you. You see the Evil Sorcerer 'Vaguely'!",
            "paths": {"south": "Misty Forest"},
            "boss": {
                "name": "Sorcerer Vaguely",
                "hp": 2, # Requires 2 hits
                "questions": [
                    ("He isn't exactly tall, but he is somewhat tall...", "tallish"),
                    ("He acts like a fool. His behavior is...", "foolish")
                ]
            }
        }
    }

    show_intro()
    
    while player.hp > 0:
        print("\n" + "-"*30)
        current_room = world[player.location]
        print(f"LOCATION: {player.location}")
        print(current_room["desc"])

        # Check for Items
        if "item" in current_room:
            slow_print(f"You found the {current_room['item']}! You can now turn base words into adjectives!")
            player.has_sword = True
            del current_room["item"] # Remove item after pickup

        # Check for Puzzles (Schoolhouse)
        if "puzzle" in current_room:
            slow_print(f"PUZZLE: {current_room['puzzle']['question']}")
            ans = input("Your Answer: ").lower().strip()
            if ans == current_room['puzzle']['answer']:
                slow_print("Correct! The magic clears.")
                del current_room["puzzle"]
            else:
                slow_print("Incorrect. The fog remains.")

        # Check for Enemy (Forest)
        if "enemy" in current_room:
            enemy = current_room["enemy"]
            slow_print(f"BATTLE: {enemy['desc']}")
            slow_print(f"HINT: {enemy['hint']}")
            
            if not player.has_sword:
                slow_print("You need the Suffix Sword to fight! Run away!")
            else:
                attack = input("Type the -ish word to attack: ").lower().strip()
                if attack == enemy['weakness']:
                    slow_print(f"You struck the enemy with {attack}! It vanished!")
                    del current_room["enemy"]
                else:
                    slow_print("That didn't work! The enemy hit you!")
                    player.hp -= 1
                    print(f"HP remaining: {player.hp}")

        # Check for Boss (Cave)
        if "boss" in current_room:
            boss = current_room["boss"]
            slow_print(f"FINAL BOSS: {boss['name']} appears!")
            
            for q_text, answer in boss['questions']:
                slow_print(f"The Boss casts a spell: '{q_text}'")
                counter = input("Counter with the -ish word: ").lower().strip()
                if counter == answer:
                    slow_print("Direct hit!")
                    boss['hp'] -= 1
                else:
                    slow_print("Missed! You took damage.")
                    player.hp -= 1
                
                if player.hp <= 0:
                    break

            if player.hp > 0 and boss['hp'] <= 0:
                slow_print("\nCONGRATULATIONS! You defeated the Sorcerer!")
                slow_print("Clarity has been restored to Suffixia.")
                break
            elif player.hp <= 0:
                slow_print("You have fallen...")
                break

        # Movement Input
        command = input("\nWhat do you want to do? ").lower().split()
        if not command: continue
        
        action = command[0]

        if action == "quit":
            print("Thanks for playing!")
            break
        elif action == "go":
            if len(command) > 1:
                direction = command[1]
                if direction in current_room["paths"]:
                    player.location = current_room["paths"][direction]
                else:
                    print("You can't go that way.")
            else:
                print("Go where?")
        elif action == "help":
            print("Try: go north, go south, go east, go west")
        elif action == "inventory":
            print(f"HP: {player.hp}")
            print(f"Weapon: {'Suffix Sword' if player.has_sword else 'None'}")
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    game_loop()
