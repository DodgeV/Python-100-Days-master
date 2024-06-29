#!/home/xzc/demo/venv/bin/python3

import random
import requests
from bs4 import BeautifulSoup


def page_count(url, version, path):
    try:
        response = requests.get(url)
        response.encoding = "gb2312"
        soup = BeautifulSoup(response.text, "html.parser")
        page = soup.find("ul", class_="pagelist")
        if not page:
            print("Pagination not found.")
            return
        count = page.find("strong").string
        page_ul = page.find("a").get("href").rsplit("_", 1)[0]
        if int(count) == 1:
            down_test(url, version, path)
        else:
            for j in range(1, int(count) + 1):
                page_url = url + "/" + page_ul + "_" + str(j) + ".html"
                down_test(page_url, version, path)
                time.sleep(random.randint(1, 5))  # 随机等待1到5秒
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")


def down_test(url, version, path):
    try:
        response = requests.get(url)
        response.encoding = "gb2312"
        soup = BeautifulSoup(response.text, "html.parser")
        test_list = soup.find("ul", class_="c1")
        test_tr = test_list.find_all("tr")
        for tr in test_tr:
            if version in tr.text:
                test_td = tr.find("a").get("href")
                name = tr.find("a").string  # 试卷的文件名
                test_url = baseurl + test_td  # 构造试卷网址
                testpage = requests.get(test_url)
                testpage_soup = BeautifulSoup(testpage.text, "html.parser")
                downurllist = testpage_soup.find("ul", class_="downurllist")
                downurl = downurllist.find("a").get("href")  # 从试卷网址获取文件下载地址
                test = requests.get(baseurl + downurl)  # 构造完整的地址并下载
                test.encoding = "gb2312"
                with open(path + "\\" + name + ".rar", "wb") as f:
                    f.write(test.content)
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return


if __name__ == '__main__':
    print("数据来源：第一试卷网(www.shijuan1.com)  仅支持个人研究和学习,商用请联系官方授权.\n")
    print("声明:本代码仅供学习研究使用,请勿用于商业用途,否则后果自负!\n")

    sb = ["语文试卷", "数学试卷", "英语试卷", "物理试卷", "化学试卷", "政治试卷", "历史试卷", "地理试卷", "生物试卷"]
    gd = "一年级  二年级  三年级  四年级  五年级  六年级  七年级  八年级  九年级  中考试卷  高一  高二  高三  高考试卷".split()

    # 定义一个字典来映射试卷类型和对应的年级列表片段  
    mapping = {
        "语文试卷": gd,
        "数学试卷": gd,
        "英语试卷": gd,
        "物理试卷": gd[7:],  # 从八年级开始  
        "化学试卷": gd[8:],  # 从九年级开始  
        "政治试卷": gd[6:],  # 从七年级开始  
        "历史试卷": gd[6:],  # 从七年级开始  
        "地理试卷": gd[6:],  # 从七年级开始 
        "生物试卷": gd[6:],  # 从七年级开始
    }

    for i in sb:
        # 使用字典来获取对应的年级列表片段并打印  
        print(f"{i}:{'  '} {' '.join(mapping[i])}")

    baseurl = "https://www.shijuan1.com"
    subject = {
        "语文试卷": '/a/sjyw', "数学试卷": '/a/sjsx', "英语试卷": '/a/sjyy', "物理试卷": '/a/sjwl', "化学试卷": '/a/sjhx',
        "政治试卷": '/a/sjzz', "历史试卷": '/a/sjls', "地理试卷": '/a/sjdl', "生物试卷": '/a/sjsw'
    }
    grade = {
        "一年级": "1", "二年级": "2", "三年级": "3", "四年级": "4", "五年级": "5", "六年级": "6", "七年级": "7",
        "八年级": "8", "九年级": "9", "中考试卷": "zk", "高一": "g1", "高二": "g2", "高三": "g3", "高考试卷": "gk"
    }
    s = input("请输入科目名称：")
    g = input("请输入年级：")
    urlDownload = baseurl + subject[s] + grade[g]
    version = input("请输入版本信息：")
    path = input("请输入要保存文件的路径：")
    page_count(urlDownload, version, path)
