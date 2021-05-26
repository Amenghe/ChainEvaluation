from Filter import remove_useless_text, cut_words, removePunctuation, remove_common_words, remove_stop_word, stem
from Jaccard import jaccard_similarity
from util import getChains, check_contain_chinese
from nltk.corpus import wordnet as wn
import jieba

from word_similarity import SimScore


def evaluate_one_chain(chain):
    score = 1
    for node in chain:
        components_count = len(node) - 2
        components_text = node[0:components_count]
        index = int(node[components_count])
        succeed_text = node[components_count+1]
        similarities = evaluate_components(components_text,succeed_text,index)
        score =  possibility(similarities,index)*score
    return score

def possibility(similarities,index):
    return pow(similarities[index],4) / +\
    sum([pow(similarity,4) for similarity in similarities])

def evaluate_components(components_text,succeed_text,index):
    '''过滤'''
    for i in range(len(components_text)):
        components_text[i] = remove_useless_text(components_text[i])

    '''全部转为小写'''
    components_text = [text.lower() for text in components_text]
    succeed_text = succeed_text.lower()
    '''全部组件文本都为空或相同'''
    if len(set(components_text)) == 1:
        return [1/len(components_text) for x in components_text]

    '''若待选组件无文本'''
    if components_text[index] == '':
        similarities = []
        for text in components_text:
            similarities.append(jaccard_similarity(text, succeed_text))
        similarities[index] = 1
        for similarity in similarities:
            if similarities[index] > similarity:
                similarities[index] = similarity
        if similarities[index] == 0:
            return [1 for i in range(similarities)]
        if similarities[index] == 1:
            similarities[index] = 0
        return similarities


    similarities = []
    for text in components_text:

        '''组件文本与后继页面标题相似'''
        if text in succeed_text.split(' ')[0] or succeed_text.split(' ')[0] in text:
            similarities.append(1)
            continue


        similarities.append(jaccard_similarity(text, succeed_text))


    '''若待选组件相似度接近平均相似度'''
    if -0.1 <= similarities[index] - sum(similarities) / len(similarities) <= 0.1:
        #中文
        if check_contain_chinese(succeed_text.split(' ')):
            components_words = []
            succeed_words = []
            for text in components_text:
                components_words.append(cut_words(text))
            succeed_words = cut_words(succeed_text)
            components_words = [removePunctuation(words) for words in components_words]
            succeed_words = removePunctuation(succeed_words)
            components_words = remove_common_words(components_words)

            for words in components_words:
                n2n = []
                for word in words:
                    one2n = []
                    for succeed_word in succeed_words:
                        one2n.append(SimScore(wn.synsets(word,lang='cmn'),wn.synsets(succeed_word,lang='cmn')))
                    if len(one2n) != 0:
                        n2n.append(sum(one2n)/len(one2n))
                    else:
                        n2n.append(0)
                if len(n2n) != 0:
                    similarities.append(max(n2n))
                else:
                    similarities.append(0)
            if len(set(similarities)) == 1 or similarities[index] == 0:
                similarities = [1 for s in similarities]
        #英文
        else:
            components_words = []
            succeed_words = []
            for text in components_text:
                components_words.append(cut_words(text))
            succeed_words = cut_words(succeed_text)
            components_words = [removePunctuation(words) for words in components_words]
            succeed_words = removePunctuation(succeed_words)
            components_words = remove_common_words(components_words)
            components_words = [remove_stop_word(words) for words in components_words]
            succeed_words = remove_stop_word(succeed_words)
            components_words = [stem(words) for words in components_words]
            succeed_words = stem(succeed_words)
            for words in components_words:
                n2n = []
                for word in words:
                    one2n = []
                    for succeed_word in succeed_words:
                        one2n.append(SimScore(wn.synsets(word), wn.synsets(succeed_word)))
                    if len(one2n) != 0:
                        n2n.append(sum(one2n) / len(one2n))
                    else:
                        n2n.append(0)
                if len(n2n) != 0:
                    similarities.append(max(n2n))
                else:
                    similarities.append(0)
            if len(set(similarities)) == 1 or similarities[index] == 0:
                similarities = [1 for s in similarities]
    return similarities


if __name__ == "__main__":
    chains,lable = getChains("Skit.csv")
    for chain in chains:
        print(evaluate_one_chain(chain),chain,"\n")