#!/usr/local/bin/python3
while True:
    x = input("输入 y/n ：")
    if x in ["n","N"]:
        break
    print("允许")
    # 输入y则回馈“允许” 输入n 则直接退出