# python-OCR
OCR 调用百度文字识别API进行OCR文字识别
## filename: OCRforbaiduapi.py
##用途：批量图片文字识别 *.jpg
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
