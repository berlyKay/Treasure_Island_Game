def print_chest():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')



def play_treasure_island():
    print_chest()
    attempts = 0
    print("Welcome to Treasure Island.\n")
    print("Your mission... \n\n ...is to find the treasure.\n")
    cross_roads = input("You have come to a cross-roads. Would you like to go left (L) or right (R)? ")
    while cross_roads.lower() != 'l' and cross_roads.lower() != 'r':
        cross_roads = input("\nPlease enter R or L ")
        attempts += 1
        if attempts >= 3:
            print("\nToo many invalid attempts.")
            attempts = 0
            try_again()
    if cross_roads.lower() == 'r':
        print("\nYou take a step forward, but the ground crumbles beneath your feet! With a scream,\nyou plummet into darkness and fall to your untimely demise.\n\n")
        try_again()
    elif cross_roads.lower() == 'l':
        print("\n\nThe left path whispers promises of safety and treasure. You proceed with determination...\n\n")
        swim_or_wait = input("You come to a beautiful, inviting lake spread before you. The blazing sun is oppressive, and you consider taking a refreshing dip. \n\nWould you like to take a swim (swim), or wait until later (wait)? ")
        while swim_or_wait.lower() != 'swim' and swim_or_wait.lower() != 'wait' and swim_or_wait.lower() != 's' and swim_or_wait.lower() != 'w':
            swim_or_wait = input("\nPlease enter swim or wait: ")
            attempts += 1
            if attempts >= 3:
                print("\nToo many invalid attempts.")
                attempts = 0
                try_again()
        if swim_or_wait.lower() == 'swim' or swim_or_wait.lower() == 's':
            print("\nYou dive into the cool water, but the ripples summon a ferocious monster trout.\nIt leaps out and swallows you whole!\n\n")
            try_again()
        elif swim_or_wait.lower() == 'wait' or swim_or_wait.lower() == 'w':
            print("\nPatience rewards you. The waters part, revealing a secret path leading to your next challenge.\n\n")
            which_door = input("You have three large doors in front of you. One is blue, one is yellow, and one is red. Which door would you like to go through? (blue, yellow, or red): ")
            while which_door.lower() != 'blue' and which_door.lower() != 'yellow' and which_door.lower() != 'red':
                which_door = input("\nPlease enter blue or yellow or red: ")
                attempts += 1
                if attempts >= 3:
                    print("\nToo many invalid attempts.")
                    attempts = 0
                    try_again()
            if which_door.lower() == 'blue':
                print("\nThe blue door creaks open, and you’re greeted by snarling beasts with glowing eyes.\nThey pounce, and your adventure ends.")
                try_again()
            elif which_door.lower() == 'red':
                print("\nAs the red door opens, a wave of searing heat engulfs you. There’s no escape from the inferno.")
                try_again()
            elif which_door.lower() == 'yellow':
                print("\nThe yellow door opens to reveal glittering treasures beyond your wildest dreams. Congratulations, you’ve found the treasure!\n")
                try_again()

def try_again():
    print('\n****** Game over ******\n\n')
    while True:
        x = input("Please press Y to try again. Press ENTER to quit. ")
        if x.lower() == "y":
            print_chest()
            play_treasure_island()
        else:
            print("\nThank you for playing Treasure Island. Have a great day!")
            break


play_treasure_island()