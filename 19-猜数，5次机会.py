#!/usr/local/bin/python3
import random
num = random.randint(1,50)
counter = 0
while counter < 5 :
    x = int(input("输入一个1-50的数字:"))
    if x > num :
        print("猜大了")
    elif x < num :
        print("猜小了")
    else:
        print("猜对了")
        break
    counter += 1
else:
    print(num)
print(num)