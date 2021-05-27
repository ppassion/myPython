# Coding : utf-8
# Author : chyh
# Date   : 2021/5/13 17:55

import os

path = "E:\迅雷下载\果 冻 传 媒【64部全集】"


def rename():
    for root, dirs, files in os.walk(path):
        # for dir in dirs:
        #     print(os.path.join(root, dir))
        for file in files:
            full_file = os.path.join(root,file)
            if full_file.endswith("TS"):
                new_full_file = full_file.replace('TS', 'ts')
                os.rename(full_file, new_full_file)


if __name__ == '__main__':
    rename()
