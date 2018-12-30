# -*- coding: UTF-8 -*-
from aip import AipOcr  
import os
import sys
import cv2

APP_ID = 'xxxxx'  
API_KEY = 'xxxx'  
SECRET_KEY = 'xxxxx'   
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
# 图像数据，base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
 
def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read()
 
for root, dirs, files in os.walk(".", topdown=False): # 该迭代类型每单元返回三个部分，我们需要的文件名在第三部分，具体参数自行了解
    for name in files:
        if 'jpg' in name: # name即为文件夹下每个文件的文件名
            filePath = os.path.join(root, name)[2:]   
            options = {  
              'detect_direction': 'true',  
              'language_type': 'CHN_ENG',  
            }  
            result = aipOcr.webImage(get_file_content(filePath),options)
            #print(result)
            for i in result['words_result']:
                sys.stdout = open("E:\工作相关\报废\创新点\Scrap_MAC.txt", "a")
                print(i['words'])
                sys.stdout.close()
