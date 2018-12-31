import os
import sys
from aip import AipOcr

APP_ID = 'xxxx'
API_KEY = 'xxxxx'
SECRET_KEY = 'xxxxxx'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """ 
def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read()
# image = get_file_content('example.jpg')

""" 调用通用文字识别，图片参数为本地图片 """
# client.basicGeneral(image);
for root, dirs, files in os.walk(".", topdown=False): # 该迭代类型每单元返回三个部分，我们需要的文件名在第三部分，具体参数自行了解
    for name in files:
        if 'jpg' in name: # name即为文件夹下每个文件的文件名
            filePath = os.path.join(root, name)[2:] 

            """ 如果有可选参数 """  
            options = {  
              'detect_direction': 'true',   #是否检测图像朝向
              'detect_language': 'true',    #是否检测语言
              'language_type': 'CHN_ENG',   #中英文混合
              'probability' : 'true',       #是否返回识别结果中每一行的置信度
            }
            """ 网络图片文字识别  aipOcr.webImage  500次/天免费 后付费  中精度 """
            #result = aipOcr.webImage(get_file_content(filePath), options)
            
            """ 通用文字识别  aipOcr.basicGeneral  50000次/天免费 低精度 """
            result = aipOcr.basicGeneral(get_file_content(filePath), options)

            """ 调用通用文字识别（高精度版） aipOcr.basicAccurate 500次/天免费 高精度 后付费 """
            # error_code': 6,无权访问
            # result = aipOcr.basicAccurate(get_file_content(filePath), options)

            print(result)
            for i in result['words_result']:
                try:
                    print(i['words'])
                    #print(decode((i['words']), encoding="utf-8"))
                    #sys.stdout = open("E:\工作相关\报废\创新点\Scrap_MAC.txt", "a")
                    fo = open("E:\工作相关\报废\创新点\Scrap_MAC.txt", "a")
                    fo.write(i['words'] + '\n')
                    fo.close()
                except ValueError as e:
                    print(e)
