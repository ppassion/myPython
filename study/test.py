# Coding : utf-8
# Author : chyh
# Date   : 2021/2/14 22:14

import time

if __name__ == '__main__':
    time1 = time.time()
    print(time1)
    time.sleep(3)
    time2 = time.time()
    print(time2)
    print(int(time2-time1))
