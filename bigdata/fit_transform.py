# Coding : utf-8
# Author : chyh
# Date   : 2021/3/3 15:30

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA


# 转换器
def dictVec():
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]
    dict_vec = DictVectorizer()
    data = dict_vec.fit_transform(data)
    print(dict_vec.get_feature_names())
    print(data.toarray())


def tfidf():
    data = ["life is short,i like python dislike dislike", "life is too long,i dislike python",
            "dislike python short like too"]
    t = TfidfVectorizer()
    data = t.fit_transform(data)
    print(t.get_feature_names())
    print(data.toarray())


def pca():
    data = [[1, 2, 3, 4], [1, 1, 1, 1], [1, 3, 5, 7]]
    # 1、实例化PCA, 小数——保留多少信息
    transfer = PCA(n_components=0.9)
    # 2、调用fit_transform
    data1 = transfer.fit_transform(data)

    print("保留90%的信息，降维结果为：\n", data1)

    # 1、实例化PCA, 整数——指定降维到的维数
    transfer2 = PCA(n_components=3)
    # 2、调用fit_transform
    data2 = transfer2.fit_transform(data)
    print("降维到3维的结果：\n", data2)


if __name__ == '__main__':
    # tfidf()
    pca()