# Coding : utf-8
# Author : chyh
# Date   : 2021/5/13 17:52

import os


def rename():
    file_list = os.listdir()
    for file in file_list:
        if file.endswith("txt"):
            new_file = file.replace('txt', 'TXT')
            os.rename(file, new_file)


if __name__ == '__main__':
    rename()
