# Coding : utf-8
# Author : chyh
# Date   : 2021/5/5 21:06

from bs4 import BeautifulSoup
from urllib import request, parse
import threading
import time
import socket
import re
import datetime

from film_bean import film_bean
from db import db_instance

socket.setdefaulttimeout(3)

baseUrl = "http://cl.298x.xyz/thread0806.php?fid=22&search=&page="


def askUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36 "
    }
    req = request.Request(url, headers=header, method="GET")
    soup = None
    somethingHappened = False
    # noinspection PyBroadException
    try:
        response = request.urlopen(req)
        soup = BeautifulSoup(response, "html.parser")
    except BaseException as err:
        somethingHappened = True
        print(err)
    except OSError as err:
        somethingHappened = True
        print(err)
    except ConnectionResetError as err:
        somethingHappened = True
        print(err)
    return soup, somethingHappened


def repeatAskUrl(url):
    while True:
        soup, somethingHappened = askUrl(url)
        if somethingHappened:
            time.sleep(5)
        else:
            break
    return soup, somethingHappened


class getDataThread(threading.Thread):
    def __init__(self, tailNumber: int):
        threading.Thread.__init__(self)
        self.threadName = "Thread-" + str(tailNumber)
        self.tailNumber = tailNumber

    def run(self) -> None:
        for i in range(0, 10):
            page_number = i * 10 + self.tailNumber
            startTime = time.time()
            add_film_of_one_page(str(page_number))
            endTime = time.time()
            print(str(page_number) + " 耗时" + str(int(endTime - startTime)) + "秒")
        print(self.threadName + " 结束")


def add_film_of_one_page(page_number: str):
    soup, somethingHappened = repeatAskUrl(baseUrl + page_number)
    tbody = soup.find_all(id='tbody')[0]
    for tr in tbody.find_all("tr", class_="tr3 t_one tac"):
        td_list = tr.find_all('td')

        title_td = td_list[1]
        title = str(title_td.a.text)
        url = str(title_td.a['href'])

        post_info_td = td_list[2]
        find_post_date = re.compile(r'\d{4}-\d{2}-\d{2}')
        post_date_str = re.findall(find_post_date, str(post_info_td))[0]
        post_date = datetime.datetime.strptime(post_date_str, '%Y-%m-%d')

        reply_td = td_list[3]
        reply_count = int(reply_td.text.strip())

        bean = film_bean(title, url, post_date, reply_count)
        db_instance.add_proxy(bean)


if __name__ == '__main__':
    threads = []
    for i in range(1, 11):
        thread = getDataThread(i)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    # db_instance.sql()
