import os

from evaluator import evaluate_one_chain
from show import showResult, showResult_1
from util import getChains

def drawer_0():
    file_names = os.listdir('./Data')
    chains = []
    labels = []
    scores = []
    false_y = [0 for i in range(10)]
    true_y = [0 for i in range(10)]
    for file in file_names:
        chain , label = getChains(file)
        chains = chains + chain
        labels = labels + label
    for i in range(len(chains)):
        score = evaluate_one_chain(chains[i])
        print('评分{0:1.3f}   {1}   链路：{2}'.format(score,labels[i],chains[i]))
        scores.append(score)
        index = int(10 * score) if score < 1  else 9
        if labels[i] == "True":
            true_y[index] += 1
        else:
            false_y[index] += 1
    sum_true = sum(true_y)
    sum_false = sum(false_y)
    true_y = [y/sum_true for y in true_y]
    false_y = [y/sum_false for y in false_y]
    showResult(true_y,True)
    showResult(false_y,False)


def drawer_1():
    '''第二种画图方法'''
    file_names = os.listdir('./Data')
    chains = []
    labels = []
    scores = []
    false_y = [0 for i in range(10)]
    true_y = [0 for i in range(10)]
    for file in file_names:
        chain, label = getChains(file)
        chains = chains + chain
        labels = labels + label
    for i in range(len(chains)):
        score = evaluate_one_chain(chains[i])
        print('评分{0:1.3f}   {1}   链路：{2}'.format(score, labels[i], chains[i]))
        scores.append(score)
        index = int(10 * score) if score < 1 else 9
        if labels[i] == "True":
            true_y[index] += 1
        else:
            false_y[index] += 1
    showResult_1(true_list=true_y, false_list=false_y)

if __name__ == "__main__":
    drawer_1()