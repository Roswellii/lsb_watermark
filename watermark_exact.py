# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 12:45
# @Author  : Zhou Yiqun
# @File    : watermark_exact.py
# @Software: PyCharm

#-- 信息提取

from PIL import Image

key= 15 # 信息长度作为公钥
b_watermark= "" # 提取的二进制信息
watermark= "" # 提取的字符信息

carrier= Image.open("lena_watermark.bmp") # 打开带水印的图片
rgb_carrier= carrier.convert("RGB") #转为RGB形式

for i in range(rgb_carrier.size[0]):# 遍历像素，提取rgb最后一位
    for j in range(rgb_carrier.size[1]):
        print(rgb_carrier.getpixel((i, j)))
        if(len(b_watermark)>=key*7): # 提取完成及时跳出
            break
        b_watermark= b_watermark + str(rgb_carrier.getpixel((i, j))[0] % 2)
        if (len(b_watermark) >= key*7):
            break
        b_watermark = b_watermark + str(rgb_carrier.getpixel((i, j))[1] % 2)
        if (len(b_watermark) >= key*7):
            break
        b_watermark = b_watermark + str(rgb_carrier.getpixel((i, j))[2] % 2)
print("--- 二进制序列 ---")
print(b_watermark)

# binary to num, then chr
print("--- 字符编码 ---")
for i in range(key):
    asc_str=""
    for j in range(7):
        asc_str= asc_str + b_watermark[i * 7 + j] # 每7bits组成一个ascii二进制值

    asc_num= int(asc_str, base=2) # 将二进制转为数字
    asc_ch= chr(asc_num) # 将数字转为字符
    print(asc_str, asc_num, asc_ch)
    watermark=watermark+ asc_ch # 将字符加入提取结果
# output result
print("--- 提取结果 ---")
print(watermark)

