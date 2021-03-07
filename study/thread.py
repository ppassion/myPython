# Coding : utf-8
# Author : chyh
# Date   : 2021/3/7 22:21

import requests
import math

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == '__main__':
    res = requests.get(url="http://127.0.0.1:8080/get_all")
    proxyIps = eval(res.text)['proxies']
    size = len(proxyIps)
    count = math.ceil(size / 5)
    splitArrays = list(chunks(proxyIps, count))
    for proxyGroup in splitArrays:
        print(proxyGroup)
