#!/usr/local/bin/python3
import random
choices = ["石头","剪刀","布"]
win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2):"""
computer = random.choice(choices)
ind = int(input(prompt))
player = choices[ind]

if player == computer:
    print("平局")
elif [player,computer] in win_list:
    print("you win")
else:
    print("you lose")
print(player,computer)