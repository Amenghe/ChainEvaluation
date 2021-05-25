from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # 计算杰卡德系数
    return 1.0 * numerator / denominator



#print("我是" in "不我是")


if __name__ == "__main__":
    print(jaccard_similarity("电脑","台式机"))
    print("中H，密码".lower())




'''
0.5714285714285714
'''