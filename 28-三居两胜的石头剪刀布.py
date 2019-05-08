#!/usr/local/bin/python3
import random
choices = ["石头","剪刀","布"]
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
z = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
x = 0
y = 0
while x < 2 and y < 2 :
    computer = random.choice(choices)
    ind = int(input(z))
    player = choices[ind]
    if player == computer:
        print("平局")
    elif [player,computer] in win_list:
        x += 1
        print("you win ")
    else:
        y += 1
        print("you lost")