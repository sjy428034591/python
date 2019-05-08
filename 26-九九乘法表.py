#!/usr/local/bin/python3
for i in range(1,10):
    for j in range(1,i + 1):
        print(str(i)+"x"+str(j)+"=",i*j,sep="",end=" ")
    print()


n = int(input("请输入一个数字："))
for x in range(1,n+1):
    for y in range(1,x+1):
        print(str(x)+"x"+str(y)+"=",x*y,sep="",end=" ")
    print()