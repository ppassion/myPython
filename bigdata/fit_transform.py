# Coding : utf-8
# Author : chyh
# Date   : 2021/3/3 15:30

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


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


if __name__ == '__main__':
    tfidf()
