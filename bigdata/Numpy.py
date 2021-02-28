# Coding : utf-8
# Author : chyh
# Date   : 2021/2/28 13:59

import numpy as np
import matplotlib.pyplot as plt


def init():
    return np.array([[80, 89, 86, 67, 79],
                     [78, 97, 89, 67, 81],
                     [90, 94, 78, 67, 74],
                     [91, 91, 90, 67, 69],
                     [76, 87, 75, 67, 86],
                     [70, 79, 84, 67, 84],
                     [94, 92, 93, 67, 64],
                     [86, 85, 83, 67, 80]])


def createArray():
    print(np.zeros([2, 3], np.int64))
    print(np.ones([2, 3], np.int64))
    print(np.linspace(0, 100, 11, dtype=np.int64))
    print(np.arange(0, 160, 11, dtype=np.int64))
    print(np.logspace(0, 100, 11))


def createRandom():
    print(np.random.uniform(0, 10, 5))
    print(np.random.randint(0, 10, 5))
    x = np.random.uniform(0, 1, 1000)
    plt.figure()
    plt.scatter([1 for i in range(1000)], x)
    plt.show()


def cal():
    stock_change = np.random.normal(0, 1, 10)
    print(stock_change)
    # stock_change = stock_change[0:5]
    # print(stock_change)
    print(stock_change > 0.5)
    print(np.all(stock_change > 0.5))
    print(np.any(stock_change > 0.5))
    print(np.where(stock_change > 0.5, "aa", "bb"))
    print(np.min(stock_change))
    print(np.max(stock_change))
    print(np.std(stock_change))
    print(np.mean(stock_change))
    print(np.argmax(stock_change))


def twoArray():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr * 2)


if __name__ == '__main__':
    # createArray()
    # createRandom()
    # cal()
    twoArray()
