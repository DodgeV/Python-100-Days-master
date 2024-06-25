'''
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

# encoding: utf-8
import collections 
import re

def countWords(input_filename, output_filename):
    try:  
        with open(input_filename, 'r', encoding='utf-8') as fp:  
            text = fp.read()  
            # 使用正则表达式去除标点符号，并将文本转换为小写  
            cleaned_text = re.sub(r'[^\w\s]', '', text.lower())  
            # 使用正则表达式分割单词  
            words = re.findall(r'\b\w+\b', cleaned_text)  
            word_counts = collections.Counter(words)  

        with open(output_filename, 'w', encoding='utf-8') as result_file:  
            for key, value in word_counts.items():  
                result_file.write(key + ':' + str(value) + '\n')  

        print(f"单词统计结果已写入到 {output_filename}")  
    except FileNotFoundError:  
        print(f"文件 {input_filename} 不存在，请检查文件名和路径是否正确。")  
    except Exception as e:  
        print(f"发生错误：{e}")

if __name__ == "__main__":
    input_filename = input('input a filename:')
    output_filename = input('output filename is:')
    countWords(input_filename, output_filename)
