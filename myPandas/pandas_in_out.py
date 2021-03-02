# Coding : utf-8
# Author : chyh
# Date   : 2021/3/2 15:21

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    stock_change = np.random.normal(0, 1, (10, 5))

    row_index = ['股票' + str(i) for i in range(1, stock_change.shape[0] + 1)]
    col_index = ['day' + str(i) for i in range(1, stock_change.shape[1] + 1)]

    stock_change = pd.DataFrame(stock_change, index=row_index, columns=col_index)
    stock_change.to_csv("./files/test.csv", index=False)

    json = '''
    {
    "employees": [
    { "firstName":"Bill" , "lastName":"Gates" },
    { "firstName":"George" , "lastName":"Bush" },
    { "firstName":"Thomas" , "lastName":"Carter" }
    ]
    }
    '''
    json_read = pd.read_json(json)
    print(json_read)
    json_read.to_json("./files/test.json")
