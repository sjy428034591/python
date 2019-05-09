#!/usr/local/bin/python3
import random
import string

chars = string.ascii_letters + string.digits

def apass(n=8):
    result = ''
    for i in range(n):
        ch = random.choices(chars)
        result += ch

    return result

if __name__ == '__main__':
    print(apass())