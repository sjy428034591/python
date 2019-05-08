#!/usr/local/bin/python3
import random
num = random.randint(1,10)
running = True
while running:
    x = int(input("请输入一个1-10的数字:"))
    if x > num :
        print("猜大了")
    elif x < num :
        print("猜小了")
    else:
        print("猜对了")
        running = False
print(num)