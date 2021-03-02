# Coding : utf-8
# Author : chyh
# Date   : 2021/3/2 15:55

import pandas as pd
import numpy as np

if __name__ == '__main__':
    stock_change1 = np.random.normal(0, 1, (10, 5))
    row_index1 = ['股票' + str(i) for i in range(1, stock_change1.shape[0] + 1)]
    col_index1 = ['day' + str(i) for i in range(1, stock_change1.shape[1] + 1)]
    stock_change1 = pd.DataFrame(stock_change1, index=row_index1, columns=col_index1)

    stock_change2 = np.random.normal(0, 1, (10, 5))
    row_index2 = ['股票' + str(i) for i in range(11, stock_change2.shape[0] + 11)]
    col_index2 = ['day' + str(i) for i in range(1, stock_change2.shape[1] + 1)]
    stock_change2 = pd.DataFrame(stock_change2, index=row_index2, columns=col_index2)

    print(stock_change1)
    print(stock_change2)
    print(pd.concat([stock_change1, stock_change2], axis=0))
