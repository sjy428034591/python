#!/usr/local/bin/python3
number = input("请输入数字: ")
print(number)
print(type(number))
   
#print(number + 10) 报错，不能把字符串和数字做运算
print(int(number) + 10)  # int可将字符串10转换成数字
print(number + str(10))  # str讲10转换为字符串后实现字符串拼接
