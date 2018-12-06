import requests
from lxml import etree
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
def spiderOnePage(url,headers):
    response=requests.get(url,headers=headers)
    #html = response.text
    page=etree.HTML(response.text)
    trList = page.xpath('//*[@id="quotesearch"]/ul[1]/li/a/text()')
    for trList_ in trList:
        print(trList_)




if __name__ == '__main__':
    #url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_BulletinGather.php?gg_date=#datetime#&page='
    url = 'http://quote.eastmoney.com/stocklist.html'
    #url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=sz000725'
    spiderOnePage(url,headers)