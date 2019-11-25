# 爬取豆瓣活动/新书两个tab页内容 https://market.douban.com/book/?type=activity&page=1&page_num=10
# 同时把数据存储到本地mysql的egg_db数据库中，表结构如下
# DROP TABLE IF EXISTS `douban_activity`;
# CREATE TABLE `douban_activity` (
#   `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '利用主键策略生成的唯一键',
#   `title` varchar(128) DEFAULT NULL COMMENT '标题',
#   `share_title` varchar(128) DEFAULT NULL COMMENT '分享标题',
#   `share_content` varchar(128) DEFAULT NULL COMMENT '分享内容',
#   `share_pics_rectangle` varchar(128) DEFAULT NULL COMMENT '分享图片',
#   `partake_counts` int(11) DEFAULT NULL COMMENT '参与人数',
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

import requests
import pymysql

# 获取数据内容，并且拼接
def get_xhr_data():
  retArr = []
  page = 1
  pageSize = 10
  total = 10
  param = { 'page': page, 'page_size': pageSize, 'type': 'activity'}
  # 递归获取列表的所有内容
  while ((page - 1) * pageSize <= total):
    reqRes = handle_request(param)
    total = reqRes['total']
    page += 1
    param['page'] = page
    retArr.extend(reqRes['data'])
  return retArr

# 进行请求
def handle_request(param):
  url = 'http://market.douban.com/api/freyr/books'
  xhr_headers = {
    'Accept': 'application/json' ,
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Host': 'market.douban.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
  }
  try:
    return requests.get(url, param, headers=xhr_headers).json()
  except:
    return []

# 获取数据库操作游标
def handle_db_connect():
  conn = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='egg_db')
  return conn

# 存储数据到sql
def handle_save_data(activityData, conn):



def main():
  activityData = get_xhr_data()
  conn = handle_db_connect()
  handle_save_data(activityData, conn)

main()