'''
 * BDImageSpider
 * 百度图片爬虫，输入关键词和数量抓取图片，使用前注意修改保存路径
 * author : Syrah (dw313@126.com)
 * 2019/9/13 00:13  江苏苏州
 *版本：V2.0.0  详细注释版
 '''

import requests
import re
import os
import random
import time

class spider(object):
    def __init__(self):
        self.url = ""
        self.key = input("下载关键词：")
        self.amount = int(input("数量："))
        if not os.path.exists(r"E:\\PJ\\图片\\" + self.key):      #路径自己定义
            os.mkdir(r"E:\\PJ\\图片\\" + self.key)

    def setUrl(self):
        result = []
        page = self.amount // 30 + 1                            #30张图是一页 page存放页数
        for i in range(1,30*page+30+1,30):                  #30张翻页一次，i控制每页第一个图片的pn
            url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+self.key+"&pn="+str(i)+"&gsm=&ct=&ic=0&lm=-1&width=0&height=0"
            r = requests.get(url)                                      #r是HTTPresponse类型，详情见https://www.cnblogs.com/mzc1997/p/7813801.html
            ret = r.content.decode()                                # r.content是r的内容，以字节流存放，这里转化字符串
            resultNow = re.findall('"objURL":"(.*?)",', ret)   #objURL存放页面下所有图片链接，提取并存放在resultNow
            #print(ret)                                                      #查看有惊喜
            result+=resultNow                                       #每页的图片列表放到总列表里
        self.download(result)


    def download(self, res):
        count = 1                        #count用于计数
        max = len(res)
        if max < self.amount:
            self.amount = max
        for i in res:                    #遍历链接列表的每个链接
            try:
                respond = requests.get(i)
            except Exception as e:
                print(e)
                continue
            name = i[-4:]                                   #文件命名
            end = re.search('\.', name)
            if end == None:
                name = ".jpg"
            path = r"E:\\PJ\\图片\\" + self.key + "\\"     # 路径自己定义
            filepath = path + str(count) + name
            print(filepath)
            with open(filepath, 'wb') as f:                 #写入
                f.write(respond.content)
            if count >= self.amount:                       #达到数量后结束
                break
            else:
                count += 1
            #randnumber1 = random.randint(0, 3)  # 生成随机数    #试图随机延迟伪装人工然而并没卵用
            #time.sleep(randnumber1)             # 按随机数延时


if __name__ == '__main__':
    do = spider()
    do.setUrl()
