import os
import sys
from aip import AipOcr

"""
filename: OCRforbaiduapi.py
用途：批量图片文字识别 *.jpg

***** 在需要识别的文件路径下执行 *****
 
百度文字识别 http://ai.baidu.com/tech/ocr
API https://console.bce.baidu.com/ai/?fromai=1#/ai/ocr/app/detail~appId=734442
错误码 http://ai.baidu.com/docs#/OCR-Python-SDK/78293940

关注公众号“百度OCR文字识别”（同时能及时获取接口升级等信息）
百度AI社区--文字识别官方版块：http://ai.baidu.com/forum/topic/list/164
具有免费调用额度的接口，超过每天的免费额度后会返回错误码：17，错误信息：Open api daily request limit reached（每天流量超限额）；
所有图片均需要base64编码、去掉编码头后再进行urlencode。
请注意：上传的图片使用JPG格式可以一定程度上提高识别准确率！
强烈建议：如果您使用OCR的服务，请从文字识别的控制台进入并创建应用

接口能力
接口名称	接口能力简要描述
通用场景文字识别	对各类通用场景、文件的识别接口，按行返回识别结果
通用文字识别	识别图片中的文字信息
通用文字识别（高精度版）	更高精度地识别图片中的文字信息
通用文字识别（含位置信息版）	识别图片中的文字信息（包含文字区域的坐标信息）
通用文字识别（高精度含位置版）	更高精度地识别图片中的文字信息（包含文字区域的坐标信息）
通用文字识别（含生僻字版）	识别图片中的文字信息（包含对常见字和生僻字的识别）
"""


""" 百度文字识别 """
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

            #print(result)
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
