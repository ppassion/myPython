# Coding : utf-8
# Author : chyh
# Date   : 2021/3/2 15:39

import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("./files/test.csv")
    print(data)
    print(data.dropna())
    # print(data.notnull(csv))
    print(data.fillna(0))
