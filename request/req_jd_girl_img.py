# 处理网站的Anti creeper防爬机制
from selenium import webdriver
# 类似jquery选择器似的，选中文档中的dom对象
from bs4 import BeautifulSoup
import requests

# 保存图片的路径
# savePath="F:/pic/" 
savePath="/Users/hf/sky/pic/"

# 需要爬取的url的地址，这里是爬了30-39页
urls = ["http://jandan.net/ooxx/page-{}#comments".format(str(i)) for i in range(30, 40)] 

driver = webdriver.Chrome()
for url in urls:
    driver.get(url)
    # 网页源码
    data = driver.page_source
    # 解析网页
    soup = BeautifulSoup(data, "lxml")
    # 定位元素
    images = soup.select("a.view_img_link")

    for image in images:
        dynamic = image.get('href')
        if str('gif') in str(dynamic): # 去除gif
            pass
        else:
            http_url = "http:" + dynamic
            img_res = requests.get(http_url)
            print('正在下载 %s' % http_url)
            with open(savePath + http_url[-15:] , 'wb') as jpg:
                jpg.write(img_res.content)