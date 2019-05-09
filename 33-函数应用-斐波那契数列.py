#!/usr/local/bin/python3
def gen_fib(l):
    fib = [0,1]
    for i in range(l - len(fib)):
        fib.append(fib[-1] + fib[-2])
    return fib
a = gen_fib(10)
print(a)
print("-" * 50)
n = int(input("length: "))
print(gen_fib(n))