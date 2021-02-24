# Coding : utf-8
# Author : chyh
# Date   : 2021/2/24 9:06

import time


def splitString(myStr):
    result = ""
    splitArray = myStr.split(",")
    for i in splitArray:
        result = result + i + str(time.time()) + "chyh" + "\n"
    return result


if __name__ == '__main__':
    print(splitString("aa,bb"))
