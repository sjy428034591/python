#!/usr/local/bin/python3
def mtable(n):
    for i in range(1,n + 1):
        for j in range(1,i + 1):
            print("%s*%s=%s" % (i, j, i * j), end=" ")
        print()
mtable(9)
mtable(int(input("输入一个数字:")))