#!/usr/local/bin/python3
#计算100以内偶数之和。
#continue是跳过本次循环剩余部分，回到循环条件处。
sum = 0
counter = 0
while counter < 100 :
    counter += 1
    if  counter % 2 == 1 :
        continue
    sum += counter
print(sum)
