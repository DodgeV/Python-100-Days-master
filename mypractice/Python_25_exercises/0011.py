'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京,程序员,公务员,领导,牛比,牛逼,你娘,你妈,love,sex,jiangge
'''
class SensitiveWordFilter(object):  
    def __init__(self, filename='filtered_words.txt'):  
        self.sensitive_words = self.load_words_from_file(filename)  
        self.user_input = ''  
        self.output_message = 'Human Rights'  

    @staticmethod  
    def load_words_from_file(filename):  
        with open(filename, 'r', encoding='utf8') as file:  
            return [line.strip() for line in file.readlines()]  

    def filter_input(self):  
        for word in self.sensitive_words:  
            if word in self.user_input:  
                self.output_message = 'Freedom'  
                return  

    def get_user_input(self):  
        self.user_input = input('请输入文字：')  

    def display_output(self):  
        self.filter_input()  
        print(self.output_message)  

    def run_interactive(self):  
        while True:  
            self.get_user_input()  
            self.display_output()  
            choice = input('再输入吗？(y/n)：').lower()  
                if choice != 'y':  
                    break  

if __name__ == '__main__':  
    filter = SensitiveWordFilter()  
    filter.run_interactive()
