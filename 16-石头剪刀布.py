#!/usr/local/bin/python3
import random
choices = ["石头","剪刀","布"]
computer = random.choice(choices)
#input(computer)
player = input("请出拳：")
if player == "石头":
    if computer == "石头":
        print("平局")
    elif computer == "剪刀":
        print("you win")
    else:
        print("tou lose")
elif player == "剪刀":
    if computer == "石头":
        print("you lose")
    elif computer == "剪刀":
        print("平局")
    else:
        print("you win")
else:
    if computer == "石头":
        print("you win")
    elif computer == '剪刀':
        print("you lose")
    else:
        print("平局")
print(computer,player)