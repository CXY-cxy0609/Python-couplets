from urllib import request                                                                               # 用于获取页面
from bs4 import BeautifulSoup                                                                            # 用于解析页面代码
import re                                                                                                # 诗词数据的文本格式处理
import jieba.analyse                                                                                     # 用于词性分析
import function                                                                                          # 引入自带库文件

def analyze(content,s):                                                                                  # 整体爬取数据词性分析函数
    s = function.conclude(s)

    File = 'freqword_' + s + '.txt'
    result_s = open(File, 'w+')
    for x in jieba.analyse.textrank(content, topK=120000, allowPOS=(s)):                                 # 写入文本文档中
        result_s.writelines(x + " ")
    result_s.close()

# ......................爬虫1............................ #

url_1 = r"http://www.360doc.com/content/18/1009/22/9570732_793386583.shtml"                              # 网页地址
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      # 伪装成浏览器
req_1 = request.Request(url=url_1, headers=headers)
req_1 = request.urlopen(req_1)
raw_html_1 = req_1.read().decode("utf8")                                                                 # 页面源代码表示
html_1 = BeautifulSoup(raw_html_1,features="html.parser")                                                # 把网页的源代码作为参数实例化
lis_1 = html_1.find_all("font",{"color":"#008000"})                                                      # 根据前端代码属性获取对联
print(lis_1)                                                                                             # 输出提示代码运行

f1 = open("coup.txt","w")                                                                               # 写入文件
for i in lis_1:
    f1.write(str(i))

f1.close()

# ......................爬虫1............................ #
'''
爬虫2与3均为在一个页面中获取索引链接，然后进入这个链接获取数据，爬虫3是进
入链接的链接获取数据
'''
# ......................爬虫2............................ #

url_21 = r"https://www.liuxue86.com/fanwen/duilian/"                                                     # 首页链接
req_21 = request.urlopen(url_21)
raw_html_21 = req_21.read().decode("utf8")
html_21 = BeautifulSoup(raw_html_21,features="html.parser")
lis_21 = html_21.find_all("ul",{"class":"grid_list"})

f2 = open("coup.txt","a")

for li_21 in lis_21:                                                                                    # 第一层for读取页面的每一个超链接
    div_2s = li_21.find_all("a")
    for div_2 in div_2s:                                                                                # 第二层for进入每个超链接的页面
        url_22 = div_2["href"]                                                                          # 为方便处理先代换

        req_22 = request.urlopen(url_22)
        raw_html_22 = req_22.read().decode("utf8")
        html_22 = BeautifulSoup(raw_html_22, features="html.parser")
        lis_22 = html_22.find_all("div", {"class": "main_zhengw"})[0]                                   # 爬取的只有一组数取，为好理解后面添[0]
        try:                                                                                            # 异常处理，有些<div>里可能没有<p>标签
            k = lis_22.find_all("p")[1:]                                                                # 找到里面的<p>标签，根据页面，第一个不是对联，所以去除
            for i in k:
                f2.write(str(i))
            print(k)
        except Exception:                                                                               # 出现各种异常都跳过并继续
            continue

f2.close()

# ......................爬虫2............................ #

# ......................爬虫3........................... #

url_31 = r"https://so.gushiwen.cn/gushi/tangshi.aspx"                                                  # 网页地址
req_31 = request.Request(url=url_31, headers=headers)
req_31 = request.urlopen(req_31)
raw_html_31 = req_31.read().decode("utf8")
html_31 = BeautifulSoup(raw_html_31,features="html.parser")
lis_31 = html_31.find_all("div",{"class":"cont"})                                                     # 先获取页面右边标签的每一个链接

f3 = open("coup.txt","a")

for li_31 in lis_31:
    a_31 = li_31.find_all("a")
    for a_311 in a_31:                                                                                # 然后进入子链接
        url_32 = a_311["href"]
        try:                                                                                          # 异常处理
            req_32 = request.urlopen(url_32)
            raw_html_32 = req_32.read().decode("utf8")
            html_32 = BeautifulSoup(raw_html_32, features="html.parser")
            lis_32 = html_32.find_all("div", {"class": "typecont"})

            for li_32 in lis_32:                                                                     # 再进入子链接里进入获取古诗词的链接
                a_32 = li_32.find_all("a")
                for a_312 in a_32:
                    url_33 = r"https://so.gushiwen.cn" + a_312["href"]
                    req_33 = request.urlopen(url_33)
                    raw_html_33 = req_33.read().decode("utf8")
                    html_33 = BeautifulSoup(raw_html_33, features="html.parser")
                    lis_33 = html_33.find_all("div", {"class": "contson"})[0]
                    try:
                        for i in lis_33:
                            f3.write(str(i))
                        print(lis_33)
                    except Exception:
                        continue
        except Exception:
            continue

f3.close()

# .....................爬虫3........................... #

# .....................文本格式处理...................... #

poemfile = open("coup.txt").read()

p1 = r"[\u4e00-\u9fa5]{4,7}[\u3002|\uff0c|\uff1f|\uff1b]"                                            # 汉字重复4-7次，中文句号，中文逗号，分号，问号
pattern1 = re.compile(p1)
result = pattern1.findall(poemfile)                                                                  # 编译正则表达式

file = open('coup.txt','w+')                                                                         #打开输出文件
for x in result:
    file.write(x)

file.close()

#.....................文本格式处理......................#

# .................诗词数据的词性分析................... #

poetry_file = 'coup.txt'
content = open(poetry_file).read()                                                                  #打开爬取的对联文件
for i in function.nature:                                                                                    #通过循环实现词性分析，提高代码质量
    analyze(content,i)

# .................诗词数据的词性分析................... #