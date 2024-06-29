#!/home/xzc/demo/venv/bin/python3
import requests
import os
import random
from PIL import Image
import numpy
import time

user_agent = ['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
              'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
              'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
              ' like Gecko) Chrome/126.0.0.0 Safari/537.36',
              'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,'
              'likeGecko)Chrome/17.0.963.56Safari/535.11',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727'
              ';SE2.XMetaSr1.0)',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
              'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,'
              'likeGecko)Version/5.1Safari/534.50']


class GetBaiduImg(object):

    def __init__(self, result, n):
        """
        :param result: 输入百度图片搜索的关键词
        :param n: 输入要爬取的页数
        """
        self.keyword = result
        self.num = n
        self.headers = {'Host': 'image.baidu.com', 'user-agent': random.choice(user_agent), 'Connection': 'keep-alive'}
        self.urls = list()

    def getPages(self):
        try:
            param = {'tn': 'resultjson_com', 'logid': '11244412704210458858','ipn': 'rj',
                      'ct': '201326592', 'is': '', 'fp': 'result', 'fr':'','word': self.keyword,'queryWord': self.keyword,
                      'cl': '2', 'lm': '-1', 'ie': 'utf-8', 'oe': 'utf-8', 'adpicid': '', 'st': '',
                      'z': '', 'ic': '', 'hd': '', 'latest': '', 'copyright': '',
                       's': '', 'se': '', 'tab': '', 'width': '', 'height': '',
                      'face': '', 'istype': '', 'qc': '', 'nc': '1', 'expermode': '','nojc':'',
                      'isAsync': '', 'pn': '0', 'rn': '30', 'gsm': '3c', '1719236329137':''}  # logid \ gsm \ 最后一个数字
            start_url = 'https://image.baidu.com/search/acjson'
            for i in range(30, self.num * 30 + 30, 30):
                param['pn'] = i
                res = requests.request(method='get', url=start_url, headers=self.headers, params=param)
                res.raise_for_status()
                res.encoding = res.apparent_encoding
                response = res.content.decode('utf-8')
                for item in response.split('"'):
                    if "https://img" in item:
                        self.urls.append(item)
            return set(self.urls)
        except requests.RequestException as e:
            print('mistake info==>', str(e))
            return set()

    def downloadJpg(self, datalist, direct='./baidu'):
        """
        根据链接列表下载图片
        :param datalist: 输入百度图片链接列表
        :param direct: 输入要保存的路径
        """
        if not os.path.exists(direct):
            os.mkdir(direct)

        for i, data in enumerate(datalist,start=1):
            filename = f'{direct}/{self.keyword}_{i}.jpg'
            print(f'Downloading img {filename}')
            try:
                resp = requests.request(method='get', url=data)
                open(filename, 'wb').write(resp.content)
                time.sleep(random.randint(1, 5))  
                print("随机等待1到5秒")
            except Exception as exp:
                print("mistake info==>", str(exp))

    def convertColor(self, direct):
        """
        将图片颜色转为灰白
        :param direct: 输入要转化的路径
        """
        for i in os.listdir(direct):
            im = numpy.array(Image.open(f'{direct}/{i}').convert('L')).astype('float')
            print(f"converting img [{i}] with ", im.shape, im.dtype)
            depth = 10
            grad = numpy.gradient(im)
            grad_x, grad_y = grad
            grad_x = grad_x * depth / 100
            grad_y = grad_y * depth / 100
            A = numpy.sqrt(grad_x ** 2 + grad_y ** 2 + 1)
            uni_x = grad_x / A
            uni_y = grad_y / A
            uni_z = 1 / A
            vec_el = numpy.pi / 2.2
            vec_az = numpy.pi / 4
            dx = numpy.cos(vec_el) * numpy.cos(vec_az)
            dy = numpy.cos(vec_el) * numpy.sin(vec_az)
            dz = numpy.sin(vec_el)
            b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
            a = b.clip(0, 255)
            im = Image.fromarray(a.astype('uint8'))
            im.save(f'{direct}/[灰度照]{i}')


if __name__ == "__main__":
    result = input('input a search keyword:')
    n = eval(input('input a num of pages:'))
    baiduimg = GetBaiduImg(result=result, n=n)
    datalist = baiduimg.getPages()
    baiduimg.downloadJpg(datalist=datalist, direct='./baidu')
    baiduimg.convertColor('./baidu')
