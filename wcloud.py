'''
数据分析和词云可视化
'''

import jieba.analyse
import matplotlib.pyplot as plt                                                                       # 绘图
import numpy as np                                                                                    # 词频分析
from PIL import Image                                                                                 # 图片处理
from wordcloud import WordCloud
import csv
import function

nature = ['a','ad','ag','an','b','c','d','df','dg','e','f','g','h','i','j','k','l','m','mg',
          'mq','n','ng','nr','nrfg','nrt','ns','nt','nz','o','p','q','r','rg','rr','rz','s',
          't','tg','u','ud','ug','uj','ul','uv','uz','v','vd','vg','vi','vn','vq','x','y','z','zg']   # 词的所有属性

for i in range(len(function.nature)):                                                                          # 根据词性类别
    try:
        file = 'freqword_' + function.nature[i] + '.txt'
        text = open(file,'rt').read()
        Excel = open('number.csv','a',newline='')                                                     # 打开表格文件，若不存在则创建
        writ = csv.writer(Excel)                                                                      # 创建一个csv的writer对象用于写每一行内容
        writ.writerow(['词语','出现次数'])                                                              # 写表格头
        words = jieba.lcut(text)
        counts = {}                                                                                   # 创建一个字典，用于对词出现次数的统计
        for word in words:
            if len(word) <= 1:
                continue
            else:
                counts[word] = counts.get(word,0) + 1
        item = list(counts.items())
        item.sort(key=lambda x: x[1], reverse=True)
        for i in range(20 if len(item) >= 20 else len(item)):
            writ.writerow(item[i])
    except Exception:
        continue

coup = open('coup.txt','rt').read()                                                                 # 总表，该块代码与上一块大同小异
Excel_t = open('number_total.csv','a',newline='')
writ_t = csv.writer(Excel_t)
writ_t.writerow(['词语','出现次数'])
words_t = jieba.lcut(coup)
counts_t = {}
for word in words_t:
    if len(word) <= 1:
        continue
    else:
        counts_t[word] = counts_t.get(word,0) + 1
item_t = list(counts_t.items())
item_t.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    writ_t.writerow(item_t[i])

                                                                                                     # 总词云
tags = jieba.analyse.extract_tags(coup, topK=500, withWeight=True)                                   # 最高获取五百个词
print(list(tags))
mask_t = np.array(Image.open('1.jpg'))
wc_t = WordCloud(font_path='STHUPO.TTF',
                max_font_size=50,
                background_color="white",
                max_words=500,
                mask=mask_t)
wc_t.generate_from_frequencies(dict(tags))
plt.figure(0)
plt.imshow(wc_t)
plt.axis("off")
plt.show()

for i in range(len(function.nature)):
    try:                                                                                              # 异常处理，显示每一种词性的词频
        file = 'freqword_' + function.nature[i] + '.txt'
        text = open(file).read()
        tags = jieba.analyse.extract_tags(text, topK=500, withWeight=True)                            # 最高获取五百个词
        print(list(tags))
        mask = np.array(Image.open('1.jpg'))
        wc = WordCloud(font_path='STHUPO.TTF',
                       max_font_size=50,
                       background_color="white",
                       max_words=500,
                       mask=mask)
        wc.generate_from_frequencies(dict(tags))
        plt.figure(i)
        plt.imshow(wc)
        plt.axis("off")
        plt.show()
    except Exception:
        continue