# Coding : utf-8
# Author : chyh
# Date   : 2021/2/14 22:14

import re

if __name__ == '__main__':
    string = '<font color="#333333"><font color="#333333"><font style="font-size:16px">'
    print(string.replace(r"<font[.*]>", ''))
    print(re.sub(r"<font.*>", '', string))
