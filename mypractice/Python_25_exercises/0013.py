'''
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-) http://tieba.baidu.com/p/2166231880
'''

import requests
import re
from urllib.parse import urljoin

class DownLoadImage(object):

    def __init__(self):
        self.urls = list()
        self.url = 'https://tieba.baidu.com/p/1710123825'
        self.headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
        self.s = requests.session()
        self.s.headers.update(self.headers)

    def get_image_url(self):
        resp = self.s.get(self.url)
        resp.raise_for_status()
        html_content = resp.text
        img_regex = r'<img[^>]+class="BDE_Image"[^>]+src="([^"]+)"'
        matches = re.findall(img_regex, html_content)
        for match in matches:
            full_url = urljoin(self.url, match)
            self.urls.append(full_url)

    def save(self):
        for i, url in enumerate(self.urls):
            print('Downloading IMG -->',url)
            try:
                resp = self.s.get(url, stream=True)  # 对于大文件，使用stream=True来分块读取
                resp.raise_for_status()  # 确保请求成功
                # 尝试从Content-Type确定文件扩展名
                content_type = resp.headers.get('Content-Type', '')
                if 'image/jpeg' in content_type:
                    ext = '.jpg'
                elif 'image/png' in content_type:
                    ext = '.png'
                else:
                    ext = '.bin'  # 默认为二进制文件
                filename = f'img{i}{ext}'
                with open(filename, 'wb') as file:
                    for chunk in resp.iter_content(1024): # 分块写入文件
                        file.write(chunk)
            except requests.RequestException as e:
                print(f"Error downloading {url}: {e}")

    def download(self):
        self.get_image_url()
        self.save()


d = DownLoadImage()
d.download()
