'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

import re

class Input(object):

    def __init__(self):
        self.filtered_words = list()
        self.in_string = ''
        self.out_string = 'Human Rights'
        self.load_filtered_words()

    def load_filtered_words(self, filename='filtered_words.txt'):
        with open(filename, 'r', encoding='utf8') as file:
            for line in file.readlines():
                self.filtered_words.append(line.strip())

    def filter_words(self):
        pattern = r'\b(' + '|'.join(re.escape(word) for word in self.filtered_words) + r')\b'  
        self.out_string = re.sub(pattern, lambda match: '*' * len(match.group(1)), self.in_string)  
        for word in self.filtered_words:
            if word in self.out_string:
                self.out_string = self.out_string.replace(word, len(word)*'*')

    def user_input(self, filename='exercise.txt'):
        if not filename:
            self.in_string = input('>')
        else:
            with open(filename, 'r', encoding='utf-8') as file:
                self.in_string = file.read()

    def std_output(self):
        self.filter_words()
        print(self.out_string)

if __name__ == '__main__':
    i = Input()
    i.user_input()
    i.std_output() 
