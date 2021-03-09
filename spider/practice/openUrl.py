# Coding : utf-8
# Author : chyh
# Date   : 2021/3/6 21:18

import webbrowser
import yaml

if __name__ == '__main__':
    configFile = open("urlInfo.yml", 'r', encoding='utf-8')
    config = configFile.read()
    configMap = yaml.load(config, Loader=yaml.FullLoader)
    posts = '''
    104404  102951  102961  103957  102909  98031  101000
104824  104658  102935  102905  102946  98102
    '''
    array = posts.split()
    print(array)
    for i in array:
        webbrowser.open(configMap["postBaseUrl"] + i)
