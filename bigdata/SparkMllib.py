# Coding : utf-8
# Author : chyh
# Date   : 2021/2/26 23:06

from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.python.pyspark.shell import spark

# sentenceData = spark.createDataFrame([
#     (0, "Hi I heard about Spark"),
#     (0, "I wish Java could use case classes"),
#     (1, "Logistic regression models are neat")
# ], ["label", "sentence"])

sentenceData = spark.createDataFrame([
    (0, "aa bb"),
    (0, "bb cc"),
    (1, "cc dd")
], ["label", "sentence"])
tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
wordsData = tokenizer.transform(sentenceData)
hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)
# CountVectorizer也可获取词频向量

idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)
for features_label in rescaledData.select("features", "label").take(3):
    print(features_label)
