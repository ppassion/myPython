# Coding : utf-8
# Author : chyh
# Date   : 2021/3/13 4:05

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self) -> None:
        print(self.threadName + " hhh")
        time.sleep(3)
        print(self.threadName + " ooo")


if __name__ == '__main__':
    thread1 = myThread("thread-1")
    thread2 = myThread("thread-2")
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
    print("aaa")
