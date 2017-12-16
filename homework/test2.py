# coding=utf-8
from PIL import Image
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
text=pytesseract.image_to_string(Image.open(r'D:\day1\homework\1.jpeg'),lang='chi_sim')
print(text)