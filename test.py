# Coding : utf-8
# Author : chyh
# Date   : 2021/2/14 22:14

import re

if __name__ == '__main__':
    content = '''
    【验证时间】：2021年2月12日<br/>
    【验证地点】：上<br/>"
    '''
    findDate = re.compile(r'验证(.*)')
    date = re.findall(findDate, content)
    print(date)
