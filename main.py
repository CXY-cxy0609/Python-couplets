import jieba.posseg                                                                         # 词性分析
import random
import pinyin
import function

def match1(word,flag):                                                                     # 整体配对（分析词性）
    flag = function.conclude(flag)                                                         # 引入函数
    files = 'freqword_' + flag + '.txt'
    res = open(files).read().split()

    while True:
        i = random.randint(0, len(res) - 1)                                                # 随机生成直至满足条件
        if len(res[i]) >= len(word):                                                       # 如果获取的词的长度大于等于分词的长度
            temp = res[i][:len(word)]
            if match2(word, temp):                                                         # 嵌套函数获得合适的词
                return str(temp)
            else:continue
        else:continue

def match2(word,temp):                                                                     # 分析平仄
    t1 = pinyin.get(temp,format="numerical")                                               # 获得词库里的词的拼音
    t2 = pinyin.get(word,format="numerical")                                               # 获得输入的分词的拼音
    l1 = []                                                                                # 记录词库拼音
    l2 = []                                                                                # 记录输入的词的拼音
    flag = 1                                                                               # 标志变量

    for x in t1:                                                                           # 将词库的声调添加进列表
        if x.isnumeric(): l1.append(x)
    for y in t2:                                                                           # 将词库的声调添加进列表
        if y.isnumeric(): l2.append(y)

    for i in range(len(l1)):
        if l2[i] == '1' or l2[i] == '2':
            if l1[i] == '3' or l1[i] == '4':
                continue
            else:
                flag = 0                                                                   # 若不满足平仄条件则返回0
                break
        else:
            if l1[i] == '1' or l1[i] == '2':
                continue
            else:
                flag = 0
                break
    return flag                                                                             # 若不满足平仄条件则返回0

couplets = input()

# ...................对输入的词性分析...................... #

res = ""
phrases = jieba.posseg.lcut(couplets)                                                       # 返回分词和词性列表

for x in phrases:
    if len(x.word) > 2 and (x.flag != 'm' or x.flag != 'mq'):                               # 为让分词更准确，分出来仍较长且不是数量词的均再次分开
        x1 = x.word[:2]
        x2 = x.word[2:]
        phrases1 = jieba.posseg.lcut(x1)
        phrases2 = jieba.posseg.lcut(x2)
        for y in phrases1:
            res += match1(y.word,y.flag)
        for z in phrases2:
            res += match1(z.word,z.flag)
    else:
        res += match1(x.word, x.flag)

# ...................对输入的词性分析......................#

print(res)