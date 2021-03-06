# Coding : utf-8
# Author : chyh
# Date   : 2021/3/6 21:18

import webbrowser
import yaml

if __name__ == '__main__':
    configFile = open("urlInfo.yml", 'r', encoding='utf-8')
    config = configFile.read()
    configMap = yaml.load(config, Loader=yaml.FullLoader)
    posts = "98849  98880  98842  98857  98859  98870  94591  94613  94604  88694  " \
            "88709  88710  88706  14025  45342  67665  67658  59203  59171  52267  " \
            "57507  57363  45275  52262  52428  52283  45303 "
    array = posts.split()
    print(array)
    for i in array:
        webbrowser.open(configMap["postBaseUrl"] + i)
