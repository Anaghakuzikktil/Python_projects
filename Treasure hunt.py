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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure")
direction=input('You\'re at a cross road. Where do you want to go? Type" "left" or "right"').lower()
if(direction=="Left"):
    decision=input("You arrive to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across").lower()
    if(decision=="wait"):
        door=input("You arrive at a island unharmed. Ther is a house with 3 doors. One red, one yellow and one blue. Which one do you choose?").lower()
        if(door=="Yellow"):
            print("You Win!")
        elif(door=="Blue"):
            print("You enter a room full of beasts. Game over!")
        elif(door=="Red"):
            print("It is a room full of fire. Game over!")
        else:
            print("You chose a door that doesn't exist. Game over!")
    else:
        print("You got attached by a Demon. Game over!")
else(direction=="Right"):
    print("Game over")
        
