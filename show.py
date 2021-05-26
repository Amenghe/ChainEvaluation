import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fmgr
def showResult(list,label):
    Songti = fmgr.FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc')
    x = [x + 0.05 for x in np.arange(0,1,0.1)]
    width = 0.09
    color = 'green'
    if label == True:
        plt.bar(x, list, color=color, width=width)
        plt.title(u'非可读文本缺失链路',fontproperties=Songti)
    else:
        plt.bar(x, list, color=color, width=width)
        plt.title(u'可读文本缺失链路', fontproperties=Songti)
        color = 'red'
    plt.xlabel(u"链路评分", fontproperties=Songti)
    plt.ylabel(u"链路占比",fontproperties=Songti)
    plt.bar(x, list, color=color, width=0.09)
    plt.show()

def showResult_1(false_list,true_list):
    Songti = fmgr.FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc')
    x = [x + 0.05 for x in np.arange(0, 1, 0.1)]
    width = 0.095
    plt.bar(x, true_list, label='非文本缺失链路', fc='green',width=width)
    plt.bar(x, false_list, bottom=true_list, label='文本缺失链路',  fc='r',width=width)
    plt.xlabel('链路评分',fontproperties=Songti)
    plt.ylabel('链路数量', fontproperties=Songti)
    height = max([max(false_list),max(true_list)])
    plt.yticks([t for t in range(0, height+1, 2)], fontsize=12)
    plt.legend(prop=Songti,loc='best')
    plt.show()

'''只显示一种颜色'''
def showResult_3(list):
    Songti = fmgr.FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc')
    x = [x + 0.05 for x in np.arange(0, 1, 0.1)]
    width = 0.095
    plt.bar(x, list, fc='green', width=width)
    plt.xlabel('链路评分', fontproperties=Songti)
    plt.ylabel('链路数量', fontproperties=Songti)
    #height = max([max(false_list), max(true_list)])
    #plt.yticks([t for t in range(0, height + 1, 2)], fontsize=12)
    #plt.legend(prop=Songti, loc='best')
    plt.show()

if __name__ == "__main__":
    l = [0.1,0.1,0,0,0,0,0,0,0,0.8]
    #showResult([0.1,0.1,0,0,0,0,0,0,0,0.8],True)
    showResult_1(l,l)

