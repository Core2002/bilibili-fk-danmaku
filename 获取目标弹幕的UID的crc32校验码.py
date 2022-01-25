# 源码来自 https://zhuanlan.zhihu.com/p/266414204

import requests
from bs4 import BeautifulSoup
import re

################ 
# 请设置参数
# 视频的CID的获取方式见cv7923601
视频的CID = ''
# 请填写目标弹幕的关键字
弹幕关键字 = ''
################

req = requests.get('https://comment.bilibili.com/'+视频的CID+'.xml')
req.encoding = req.apparent_encoding
soup = BeautifulSoup(req.text, 'html.parser').find_all(name='d')
result = ""
for i in soup:
    s = re.sub('<(.*?)>', '', str(i))
    index = 0
    if(len(弹幕关键字) > 0):
        index = s.find(str(弹幕关键字))
    if(index != -1):
        result += str(i).split(",")[6]+","+s+","+str(i).split(",")[4]+","
print('这个是crc32->', result)
