# 在百度上搜索fate图片
import requests

# URL、关键字、每页多少数据、图片数量、xhr网络请求头、图片请求头
url = 'http://image.baidu.com/search/acjson'
page_size = 30
img_count = 1
keyword = 'fate'
param = {
    'tn': 'resultjson_com' ,
    'ipn': 'rj' ,
    'ct': '201326592' ,
    'is': '' ,
    'fp': 'result' ,
    'queryWord': keyword ,
    'cl': '2' ,
    'lm': '-1' ,
    'ie': 'utf-8' ,
    'oe': 'utf-8' ,
    'adpicid': '' ,
    'st': '-1' ,
    'z': '' ,
    'ic': '0' ,
    'word': keyword ,
    's': '' ,
    'se': '' ,
    'tab': '' ,
    'width': '' ,
    'height': '' ,
    'face': '0' ,
    'istype': '2' ,
    'qc': '' ,
    'nc': '1' ,
    'fr': '' ,
    'rn': page_size 
}
xhr_headers = {
    'Accept': 'text/plain, */*; q=0.01' ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate' ,
    'Upgrade-Insecure-Requests': '1' ,
    'X-DevTools-Emulate-Network-Conditions-Client-Id': 'E546AEC93FCD78EFBB00B400338CCC19'
}
Img_headers = {
    'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=fate&oq=fate&rsp=-1' ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# 获取baidu图片接口的返回值
def get_xhr_data(pageNum):
    req_param = param.copy()
    req_param['pn'] = page_size * pageNum
    res = requests.get(url, req_param, headers=xhr_headers)
    try:
        resJson = requests.get(url, req_param, headers=xhr_headers).json()
        return resJson['data']
    except:
        return []
    

# 根据图片列表下载图片到F:/pic/文件夹中
def down_load_img(imgObjArr):
    global img_count
    for imgObj in imgObjArr:
        if 'middleURL' in imgObj:
            bin = requests.get(imgObj['middleURL'], headers=Img_headers).content
            # mac
            # with open('/Users/hf/sky/pic/%s.jpg' % img_count, 'wb') as file:
            # windows
            with open('F:/pic/%s.jpg' % img_count, 'wb') as file:
                file.write(bin)
                img_count += 1
                print(img_count)

# 主入口
def main():
    for page_num in range(20):
        imgObjArr = get_xhr_data(page_num + 1)
        down_load_img(imgObjArr)


main()


        



