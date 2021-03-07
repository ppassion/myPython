# Coding : utf-8
# Author : chyh
# Date   : 2021/3/7 21:23
import _thread

import requests
import socket
import time
import yaml
import math

socket.setdefaulttimeout(10)


def genProxies(url):

    res = requests.get(url="http://127.0.0.1:8080/get_all")
    proxyIps = eval(res.text)['proxies']
    size = len(proxyIps)
    print("共有" + str(size) + "个IP")
    groupCount = 5
    groupSize = math.ceil(size / groupCount)
    print("共有" + str(groupCount) + "个组")
    splitArrays = list(chunks(proxyIps, groupCount))
    try:
        _thread.start_new_thread(cycleAsk, ("Thread-1", splitArrays[0], url))
        _thread.start_new_thread(cycleAsk, ("Thread-2", splitArrays[1], url))
        _thread.start_new_thread(cycleAsk, ("Thread-3", splitArrays[2], url))
        _thread.start_new_thread(cycleAsk, ("Thread-4", splitArrays[3], url))
        _thread.start_new_thread(cycleAsk, ("Thread-5", splitArrays[4], url))
    except:
        print("Error: 无法启动线程")
    while 1:
        pass


def cycleAsk(threadName, proxyGroup, url):
    print(threadName)
    size = len(proxyGroup)
    for i in range(0, size):
        ip = proxyGroup[i]
        proxies = {
            "http": ip
        }
        askUrl(url, proxies)
        print(threadName + " 第" + str(i + 1) + "个IP " + ip + " 完成")


def askUrl(url, proxies):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36 "
    }
    try:
        requests.get(url, headers=head, proxies=proxies)
    except BaseException as e:
        # print(url)
        print(e)
        # somethingHappened = True
    except OSError as e:
        # print(url)
        print(e)
        # somethingHappened = True
    except ConnectionResetError as e:
        # print(url)
        print(e)
        # somethingHappened = True
    except socket.timeout as e:
        print(e)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == '__main__':
    configFile = open("../practice/urlInfo.yml", 'r', encoding='utf-8')
    config = configFile.read()
    configMap = yaml.load(config, Loader=yaml.FullLoader)
    genProxies(configMap["spreadUrl"])
