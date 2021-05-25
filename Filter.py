#!/user/bin/python
import re
import string

import jieba
import numpy as np
from nltk import WordNetLemmatizer, SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import wordnet as wn, stopwords


# #去除重复文本
# def remove_duplication(s1,s2):
#     intersection = set(s1)&set(s2)
#     s1 = set(s1).difference(intersection)
#     s2 = set(s2).difference(intersection)
#     return ''.join(list(s1)),''.join(list(s2))
#
# def remove_duplications(texts):
#     intersection = set(texts[0])
#     for text in texts:
#         intersection = intersection&set(text)
#     intersection = ' '.join(list(intersection))
#     for i in range(len(texts)):
#         texts[i] = remove_duplication(texts[i],intersection)
#     return texts

def remove_useless_text(s):
    useless_text = ['点按两次即可激活','按钮','在列表中','菜单项','无标签']
    for text in useless_text:
         s = s.replace(text,'')
    return s


def remove_stop_word(words,lang='english'):
    stop = set(stopwords.words(lang))
    filter = [word for word in words if word not in stop]
    return filter


def stem(words,lang='english'):
    stemmer = SnowballStemmer(lang)
    return [stemmer.stem(word) for word in words]

def lower(words):
    return [word.lower() for word in words]


def removePunctuation(words,lang='english'):

    punctuation = "，。？；'！\“."
    words = [word for word in words if word not in punctuation]
    if lang == 'chinese':
        return words
    return [word for word in words if word not in string.punctuation]

def cut_words(text,lang='english'):
    if lang == 'english':
        return text.split(' ')

    return list(jieba.cut(text))

def remove_common_words(component_words):
    if len(component_words) == 0:
        return []
    common_words = set(component_words[0])
    for words in component_words:
        common_words = common_words.intersection(set(words))
    for i in range(len(component_words)):
        component_words[i] = [word for word in component_words[i] if word not in common_words]
    return component_words

if __name__ == "__main__":
    # words = ["working","。","HELLO","is"]
    # words = remove_stop_word(words,'english')
    # words = stem(words,'english')
    # words = lower(words)
    # words = removePunctuation(words)
    # print(words)
    print(remove_common_words([["真的","b"],["真的","c"]]))