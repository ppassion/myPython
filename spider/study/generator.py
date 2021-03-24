# Coding : utf-8
# Author : chyh
# Date   : 2021/3/24 22:26

import time

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        print('d' + str(time.time()))
        yield b


if __name__ == '__main__':
    print('a' + str(time.time()))
    r = fibonacci(10)
    print('b' + str(time.time()))
    for i in r:
        print('c' + str(time.time()))
        print(i)
