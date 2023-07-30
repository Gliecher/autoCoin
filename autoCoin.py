# -*- coding=utf-8 -*-
import requests, re, time

# 这里填入up主的uid
uid = '652137183'

# 这里填写你自身的 cookies
cookies = {
    'DedeUserID': '94560450',
    'bili_jct': '7ef95826f238f246a4cfe8c1dfcced3e',
    'SESSDATA': '4e97f281%2C1706188888%2C554a5%2A72Q2jOtfntFy3OAgB6bvxeLMmVx4aefB3PLYQaAZzYIU0fuYwnQ_Ynxza40IKfXHaz5ohpswAAMgA'
}

# 这里填写你当前需要投币的视频的总页数 + 1
page_num = 4

# 以下代码如果没有必要, 请勿修改 ~

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "api.bilibili.com",
    "Cache-Control": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://www.bilibili.com",
}

def coining(av):
    headers['Referer'] = "https://www.bilibili.com/video/av" + str(av)
    prompt_data = {
        'aid': str(av),
        'multiply': '2',
        'select_like': '1',
        'cross_domain': 'true',
        'csrf': cookies['bili_jct']
    }
    test_page = requests.post(
        "https://api.bilibili.com/x/web-interface/coin/add",
        data=prompt_data,
        headers=headers,
        cookies=cookies
    )
    print(test_page.text)


for i in range(1, page_num):
    vpage = requests.get('https://api.bilibili.com/x/space/wbi/arc/search?mid=' + uid + '&pn=' + str(i),
                         headers=headers).text
    # print('vpage----' + vpage)
    av_list_tmp = re.compile(r"\"aid\":(\w+)").findall(vpage)
    for av in av_list_tmp:
        print('当前的av号: av' + av)
        coining(av)
        print('等待下一个视频加载...')
        time.sleep(100)
