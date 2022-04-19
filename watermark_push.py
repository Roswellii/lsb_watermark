# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 12:07
# @Author  : Zhou Yiqun
# @File    : watermark_push.py
# @Software: PyCharm

#-- 信息隐藏

from PIL import Image
# transfer watermark text into binary sequence
text= "CQUWATERMASKEXP" # 水印内容
key= len(text) # 水印长度作为公钥
print("key=",key)
b_text=""
for ch in text: # 提取每一个字符
    b_text=b_text+ bin(ord(ch)).replace('0b','').zfill(7) # 将字符转为7bits的二进制序列后合并

# open pic and convert to RGB
carrier= Image.open('lena_color.bmp')
rgb_carrier= carrier.convert('RGB') # 以RGB模式打开

# set LSB to zero
for i in range(rgb_carrier.size[0]): # 将图片每个像素rgb三元组的最后一位全部置零
    for j in range(rgb_carrier.size[1]):
        r = rgb_carrier.getpixel((i,j))[0]
        g = rgb_carrier.getpixel((i, j))[1]
        b = rgb_carrier.getpixel((i, j))[2]
        if(r%2==1):
            r=r-1
        if (g % 2 == 1):
            g = g - 1
        if (b % 2 == 1):
            b = b - 1
        rgb_carrier.putpixel((i,j), (r,g,b))

# push back watermark into pic
cur= 0
for i in range(rgb_carrier.size[0]):
    for j in range(rgb_carrier.size[1]):
        print(rgb_carrier.getpixel((i, j)))
        if(cur>= len(b_text)): # 指针越界及时跳出
            break
        r = rgb_carrier.getpixel((i, j))[0]+ (ord(b_text[cur])-ord('0')) # 将水印写入最后一位
        if (cur+1 >= len(b_text)):
            break
        g = rgb_carrier.getpixel((i, j))[1]+ (ord(b_text[cur+1])-ord('0'))
        if (cur+2 >= len(b_text)):
            break
        b = rgb_carrier.getpixel((i, j))[2]+ (ord(b_text[cur+2])-ord('0'))
        cur= cur+ 3
        rgb_carrier.putpixel((i, j), (r, g, b))
rgb_carrier.save("lena_watermark.bmp") # 保存带水印的图片



