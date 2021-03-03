# Coding : utf-8
# Author : chyh
# Date   : 2021/3/2 17:17

from sklearn import datasets
from sklearn.model_selection import train_test_split
import scipy

if __name__ == '__main__':
    iris = datasets.load_iris()
    # print(len(iris.data))
    # print(iris.data)
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target,test_size=0.2)
    print(len(x_train))
