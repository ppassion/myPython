# Coding : utf-8
# Author : chyh
# Date   : 2021/3/2 15:47

import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = np.random.uniform(150, 200, 10)
    data = pd.DataFrame(data)
    bins = [150, 160, 170, 180, 190, 200]
    cut = pd.cut(data[0], bins)
    print(cut.value_counts())
    print(pd.get_dummies(cut))
