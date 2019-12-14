# 帮哥哥他们爬证券信息
import requests
import pymysql


# 股票代码
codeArr = 'sz300760'
# 请求host
host = 'http://f10.eastmoney.com/'
# 营业总收入uri
uri1 = 'NewFinanceAnalysis/MainTargetAjax'
key = 'yyzsr'

# 获取数据
def getData():
  url = host + uri1
  xhr_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'f10.eastmoney.com',
    'If-Modified-Since': 'Sat, 14 Dec 2019 03:11:28 GMT',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
  }
  try:
    return requests.get(url, { 'type': 1, 'code': codeArr }, headers=xhr_headers).json()
  except Exception:
    print(Exception.message)
    return []


# 主函数
def main():
  ret = getData()
  print(ret)

main()