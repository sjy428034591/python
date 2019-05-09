from random import choice
import string

all_chs = string.ascii_letters + string.digits  # 大小写字母加数字

def gen_pass(n=8):
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    print(gen_pass())
    print(gen_pass(4))
    print(gen_pass(10))