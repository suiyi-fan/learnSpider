import requests as re
from lxml import etree


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

url = 'http://www.qiushibaike.com/text'
webdata = re.get(url,headers=headers)
#print webdata.text
elem = etree.HTML(webdata.text)
result = etree.tostring(elem)
tags = elem.xpath('//div[@class="article block untagged mb15"]')
name = elem.xpath('//*[@id="qiushi_tag_121295843"]/div[1]/a[2]/h2')
for tag in elem.xpath('//div[@class="article block untagged mb15"]/div[1]/a[2]/h2'):
    quote = tag.xpath('./text()')[0]
    print quote