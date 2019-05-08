#!/usr/local/bin/python3
fib = [0,1]
for i in range(8): #因为fib里面有两位数字，所以range中10个数需要减去2个
    fib.append(fib[-1] + fib[-2]) # append是在列表得末尾添加新的对象
print(fib)