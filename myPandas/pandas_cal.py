# Coding : utf-8
# Author : chyh
# Date   : 2021/3/1 23:30


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    stock_change = np.random.normal(0, 1, (10, 5))

    row_index = ['股票' + str(i) for i in range(1, stock_change.shape[0] + 1)]
    col_index = ['day' + str(i) for i in range(1, stock_change.shape[1] + 1)]

    stock_change = pd.DataFrame(stock_change, index=row_index, columns=col_index)

    print(stock_change)
    # print(stock_change['day2'].add(1))
    # twoMinusOne = stock_change['day2'].sub(stock_change['day1'])
    # stock_change['twoMinusOne'] = twoMinusOne
    # print(stock_change)
    # stock_change['day1>1'] = (stock_change['day1'] > 1)
    # print(stock_change)
    # print(stock_change[stock_change['day1'] > 1])
    # print(stock_change.query('day1 > 1'))
    # print(stock_change.describe())
    # print(stock_change.max())
    print(stock_change.cumsum())
    ss = stock_change['day1']
    ss.cumsum().plot()
    plt.show()
