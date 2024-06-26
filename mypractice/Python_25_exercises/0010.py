'''
第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
参考廖雪峰代码：liaoxuefeng.com/…/00140767171357714f87a053a824ffd811d98a83b58ec13000
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def captchaImage():
    # 240 x 60:
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('SimHei.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    # 保存图片
    image.save('code.jpg', 'jpeg');
    # 显示图片（注意：在Jupyter Notebook等环境中可能需要不同的显示方法）
    image.show()

if __name__ == "__main__":
    captchaImage()
