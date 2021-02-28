# Coding : utf-8
# Author : chyh
# Date   : 2021/2/27 19:00

import matplotlib.pyplot as plt
import random


def plot():
    plt.figure()
    plt.plot([1, 2, 3, 4, 5, 6, 7], [17, 17, 18, 15, 11, 11, 13])
    plt.show()


def savefig():
    plt.figure(figsize=(80, 8), dpi=800)
    plt.plot([1, 2, 3, 4, 5, 6, 7], [17, 17, 18, 15, 11, 11, 13])
    plt.savefig("img3.png")


def randomTemperature():
    x = range(60)
    y = [random.uniform(15, 18) for i in x]
    y_2 = [random.uniform(5, 8) for i in x]
    x_ticks_label = ["13:{}".format(i) for i in x]
    y_ticks_label = range(40)
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label="city1")
    plt.plot(x, y_2, label="city2", color='g', linestyle="--")
    plt.xticks(x[::5], x_ticks_label[::5])
    plt.yticks(y_ticks_label[::5])
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("temperature")
    plt.title("THE GRAPH")
    plt.legend(loc="lower left")
    plt.show()


def multipleAxes():
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    x = range(60)
    y = [random.uniform(15, 18) for i in x]
    y_2 = [random.uniform(5, 8) for i in x]
    axes[0].plot(x, y, label="city1")
    axes[1].plot(x, y_2, label="city2")
    axes[0].legend()
    axes[1].legend()
    fig.show()
    plt.show()


# 散点图
def scatter():
    x = [225.98, 247.07, 253.14, 457.85, 241.58, 301.01, 20.67, 288.64,
         163.56, 120.06, 207.83, 342.75, 147.9, 53.06, 224.72, 29.51,
         21.61, 483.21, 245.25, 399.25, 343.35]
    y = [196.63, 203.88, 210.75, 372.74, 202.41, 247.61, 24.9, 239.34,
         140.32, 104.15, 176.84, 288.23, 128.79, 49.64, 191.74, 33.1,
         30.74, 400.02, 205.35, 330.64, 283.45]
    plt.scatter(x, y)
    plt.show()


# 柱状图
def bar():
    x = range(5)
    y_1 = [2, 5, 4, 1, 3]
    y_2 = [3, 6, 5, 2, 4]
    plt.bar(x, y_1, width=0.2)
    plt.bar([i + 0.2 for i in x], y_2, width=0.2)
    plt.show()


# 直方图
# hist

# 饼图
def pie():
    x = range(5)
    y_1 = [2, 5, 4, 1, 3]
    plt.pie(y_1,labels=x)
    plt.show()


if __name__ == '__main__':
    # plot()
    # savefig()
    # randomTemperature()
    # multipleAxes()
    # scatter()
    # bar()
    pie()
