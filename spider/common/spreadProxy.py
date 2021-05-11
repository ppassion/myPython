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
groupCount = 20


def genProxies(url):
    global groupCount
    res = requests.get(url="http://127.0.0.1:8080/get_all")
    proxyIps = eval(res.text)['proxies']
    size = len(proxyIps)
    print("共有" + str(size) + "个IP")
    groupSize = math.ceil(size / groupCount)
    print("共有" + str(groupCount) + "个组")
    splitArrays = list(chunks(proxyIps, groupSize))
    try:
        # _thread.start_new_thread(cycleAsk, ("Thread-1", splitArrays[0], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-2", splitArrays[1], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-3", splitArrays[2], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-4", splitArrays[3], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-5", splitArrays[4], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-6", splitArrays[5], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-7", splitArrays[6], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-8", splitArrays[7], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-9", splitArrays[8], url))
        # _thread.start_new_thread(cycleAsk, ("Thread-10", splitArrays[9], url))
        for i in range(0, groupCount):
            _thread.start_new_thread(cycleAsk, ("Thread-" + str(i + 1), splitArrays[i], url))
    except:
        groupCount = groupCount - 1
        print("Error: 无法启动线程")
    while groupCount > 10:
        pass


def cycleAsk(threadName, proxyGroup, url):
    global groupCount
    size = len(proxyGroup)
    for i in range(0, size):
        ip = proxyGroup[i]
        proxies = {
            "http": ip
        }
        askUrl(url, proxies)
        # print(threadName + " 第" + str(i + 1) + "个IP " + ip + " 完成")
    print(threadName + "全部结束")
    groupCount = groupCount - 1
    print(groupCount)


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
    configFile = open("../red/urlInfo.yml", 'r', encoding='utf-8')
    config = configFile.read()
    configMap = yaml.load(config, Loader=yaml.FullLoader)
    while True:
        genProxies(configMap["spreadUrl"])
        print("============================")
        time.sleep(5)
        groupCount = 20
