import csv

'''
#从具体某一个表中获取一条链路
def getChain(filename,sheet_index):
    workbook = xlrd.open_workbook('./Data/'+filename)
    sheet = workbook.sheet_by_index(sheet_index)
    chain = []
    for i in range(sheet.nrows):
        chain.append([cell.value for cell in sheet.row(i)])
    return chain

#从工作簿种获取所有链路
def getChains(filename):
    workbook = xlrd.open_workbook('./Data/' + filename)
    sheet_names = workbook.sheet_names()
    chains = []
    for i in range(len(sheet_names)):
        chains.append(getChain(filename,i))
    return chains
'''
def getChains(filename):
    with open('./Data/'+filename,encoding='utf-8') as f:
        f_csv = csv.reader(f)
        chains = []
        chain = []
        label = []
        for row in f_csv:
            if len(row) == 0:
                break
            if row[0] == 'True' or row[0] == "False":
                chains.append(chain.copy())
                chain.clear()
                label.append(row[0])
                continue
            chain.append(row)
        return chains,label

def check_contain_chinese(check_str):
    for sentence in check_str:
        for ch in sentence:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
    return  False

if __name__ == "__main__":
    print(check_contain_chinese(["hello真的",'hello']))