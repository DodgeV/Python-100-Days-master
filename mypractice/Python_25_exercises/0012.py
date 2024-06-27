'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

class SensitiveWordFilter:
    def __init__(self, filename):
        self.sensitive_words = list()
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                words = line.strip().split(',')
                self.sensitive_words += words   # 直接相加即可合并列表

    def filter_words(self, text):
        for word in self.sensitive_words:
            text = text.replace(word, '*' * len(word))
        return text


# 使用示例
filter_obj = SensitiveWordFilter('filtered_words.txt')
user_input = input("请输入一段文字：")
filtered_text = filter_obj.filter_words(user_input)
print(filtered_text)
