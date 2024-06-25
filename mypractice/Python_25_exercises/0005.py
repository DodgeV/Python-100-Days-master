'''
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
from PIL import Image
import os

def resize(dirPath, size_x, size_y):
    """
    dirPath:目标文件夹的路径
    size_x:宽
    size_y:高
    """
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == '.jpg':
            img = Image.open(dirPath + '/' + i)
            img.thumbnail((size_x, size_y))
            img.save(dirPath + '/' + i)
            print(f"Resized: {i}")

if __name__ == "__main__":
    resize('./image', 1136, 640)
