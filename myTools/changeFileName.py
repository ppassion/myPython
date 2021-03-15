# Coding : utf-8
# Author : chyh
# Date   : 2021/3/14 21:02

import os
import re

if __name__ == '__main__':
    # path = "E:/3/唐哥/"
    # fileList = os.listdir(path)
    # i = 1
    # for file in fileList:
    #     os.rename(path + file, path + file + str(i))
    # i = i + 1
    i = 1
    array = ["aa.mp4", "bb.rmvb"]
    for file in array:
        print(re.match('(.*?)\.', file))
