# Coding : utf-8
# Author : chyh
# Date   : 2021/3/7 21:23

import requests
import socket
import time
import yaml

somethingHappened = False
socket.setdefaulttimeout(10)


def genProxies(url):
    global somethingHappened
    res = requests.get(url="http://127.0.0.1:8080/get_all")
    proxyIps = eval(res.text)['proxies']
    size = len(proxyIps)
    print("共有" + str(size) + "个IP")
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36', 'Connection': 'keep-alive'}
    for i in range(0, size):
        ip = proxyIps[i]
        proxies = {
            "http": ip
        }
        while True:
            somethingHappened = False
            askUrl(url, proxies)
            if somethingHappened:
                # print("出事了,等5秒")
                time.sleep(5)
            else:
                break
        print("第" + str(i + 1) + "个IP " + ip + " 完成")


def askUrl(url, proxies):
    global somethingHappened
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36 "
    }
    try:
        requests.get(url, headers=head, proxies=proxies)
    except BaseException as e:
        # print(url)
        # print(e)
        somethingHappened = True
    except OSError as e:
        # print(url)
        # print(e)
        somethingHappened = True
    except ConnectionResetError as e:
        # print(url)
        # print(e)
        somethingHappened = True
    except socket.timeout as e:
        # print(url)
        # print(e)
        somethingHappened = True


if __name__ == '__main__':
    genProxies("http://xiaohongloubb.com/?fromuid=400989")
