'''
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''
# !/home/xzc/demo/venv/bin/python3.6
# -*- coding: UTF-8 -*-

from PIL import Image, ImageDraw, ImageFont
# PIL https://pillow.readthedocs.org/

def add_num(img):
    # 创建一个绘画对象针对参数开始绘画
    draw = ImageDraw.Draw(img)
    # 加载TrueType或OpenType字体文件，并创建一个字体对象。
    myfont = ImageFont.truetype('./SimHei.ttf', size = 50)
    # 加载字体颜色
    fillcolor = "#008c8c"
    # 加载图片宽和高 
    width, height = img.size
    # 在图片上画上字,坐标原点为图片左上角
    draw.text((width-20, 0), '0', font = myfont, fill = fillcolor)
    # 保存图片
    img.save('./result.jpg','jpeg')
    return 0

if __name__ == "__main__":
    image = Image.open('./image.jpg')
    print(image.format,image.size,image.mode)
    add_num(image)
