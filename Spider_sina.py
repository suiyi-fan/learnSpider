#coding:utf-8
import requests
from lxml import etree
import chardet

'''
lxml 爬取
爬取 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=sz000725&Page=1' (新浪金东方A)
个股资讯  及  个股资讯内容（忽略图片）
'''
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

weblist = []

def spiderOnePage(url,headers):
    website='http://vip.stock.finance.sina.com.cn'

    response=requests.get(url,headers=headers)
    page=etree.HTML(response.text)
    print(type(page))
    print(len(page))

    trList = page.xpath('//div[@class="datelist"]/ul/a')
    #print(trList)
    print len(trList)
    for trList_ in trList:
        print(type(trList_))
        #print(isinstance(trList_,unicode))
        print(trList_.text.encode('iso-8859-1').decode('gbk').encode('utf-8'))
        #print(trList_.xpath('@href'))
        weblist.append(trList_.xpath('@href'))

def getOnePage(url,headers):
    '''
    当 遇到 <p>标签下有<span>标签导致不能获取完整的段落时可以用  page.xpath('string(.)')处理

    网页里 编码为 unicode 可以用 page.encode('iso-8859-1').decode('utf-8').encode('utf-8')转码
                                page.encode('iso-8859-1').decode('gbk').encode('utf-8')

    '''
    re = requests.get(url,headers = headers)
    selector = etree.HTML(re.text)
    pages = selector.xpath('//div[@class="article"]/p')
    print(pages)
    for page in pages:
        page = page.xpath('string(.)')
        if page is not None:
            #print(isinstance(page,unicode))
            print(page.encode('iso-8859-1').decode('utf-8').encode('utf-8'))




if __name__ == '__main__':
    #url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_BulletinGather.php?gg_date=#datetime#&page='
    #url = 'http://quote.eastmoney.com/stocklist.html'
    url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=sz000725#&page=1'
    spiderOnePage(url,headers)
    print('len=='+str(len(weblist)))
    # for i in weblist[5:10]:
    #     print(i[0])
    #     getOnePage(i[0],headers)
    getOnePage('https://finance.sina.com.cn/stock/hyyj/2018-12-06/doc-ihprknvt3181927.shtml',headers)