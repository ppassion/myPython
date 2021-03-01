# Coding : utf-8
# Author : chyh
# Date   : 2021/3/1 23:18

import pandas as pd
import numpy as np

if __name__ == '__main__':
    stock_change = np.random.normal(0, 1, (10, 5))

    row_index = ['股票' + str(i) for i in range(1, stock_change.shape[0] + 1)]
    col_index = pd.date_range('2021-03-01', periods=stock_change.shape[1], freq='B')

    stock_change = pd.DataFrame(stock_change, index=row_index, columns=col_index)
    # print(stock_change)
    # print(stock_change['2021-03-02'])
    # print(stock_change.loc['股票1'])

    # stock_change['2021-03-02'] = 1
    # print(stock_change)

    # print(stock_change.sort_values(by=['2021-03-01','2021-03-02'],ascending=True))
    print(stock_change.sort_index(ascending=False))
