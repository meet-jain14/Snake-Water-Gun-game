"""
1 for snake
0 for gun
-1 for water
Snake vs. Water: Snake wins. 1 vs -1 = 1
Water vs. Gun: Water wins. 0 vs -1 = -1
Gun vs. Snake: Gun wins. 0 vs 1 = 0
"""

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice: ")
youDict = { "s":1,
            "g":0 ,
            "w":-1 }
reverseDict = { 1:"Snake",
                0:"Gun" ,
               -1:"Water" }
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if computer == you :
    print("It's a Draw")
else:
    """if(computer-you) == -1 or (computer - you) == 2:print("You LOSE")
       else:print("You WINNN")""" #if you don't want to use below-mentioned if-elif-else ladder than use this two lines of if else instead.
    if   computer == -1 and you == 1 :
        print("Congratulations!! You WINNN")
    elif computer == -1 and you == 0:
        print("Sorry!! You LOSE")
    elif   computer == 1 and you == -1 :
        print("Sorry!! You LOSE")
    elif computer == 1 and you == 0:
        print("Congratulations!! You WINNN")
    elif computer == 0 and you == -1:
        print("Congratulations!! You WINNN")
    elif computer == 0 and you == 1:
        print("Sorry!! You LOSE")
    else:
        print("Something Went Wrong")
print("Wohoo!! Your First Project")