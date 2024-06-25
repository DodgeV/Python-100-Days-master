'''
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
# encoding: utf-8
import collections
import os.path
import re
from string import punctuation

# 常见的英文停用词列表  
STOPWORDS = set(['the', 'her', 'his', 'and', 'she', 'it', 'to', 'a', 'an', 'in', 'on', 'is', 'its', 'that', 'for', 'are', 'was', 'were', 'will', 'be', 'have', 'has', 'do', 'does', 'did', 'at', 'by', 'from', 'with', 'as', 'of', 'this', 'these', 'those', 'they', 'their', 'them', 'or', 'but', 'if', 'then', 'so', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'than', 'too', 'very', 'can', 'may', 'must', 'should', 'would', 'am', 'could', 'might', 'shall', 'will', 'would', 'about', 'after', 'again', 'also', 'an', 'another', 'any', 'because', 'before', 'between', 'both', 'but', 'by', 'came', 'can', 'come', 'could', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'he', "he's", 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'in', 'into', 'is', 'it', "it's", 'its', 'itself', 'just', 'like', 'make', 'many', 'me', 'might', 'more', 'most', 'much', 'must', 'my', 'myself', 'never', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', "she's", 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'these', 'they', "they're", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'would', 'you', 'your', 'yours', 'yourself', 'yourselves'])  

def judgeit(words):
    for i in range(6):
        if len(words[i]) > 2 and words[i] != 'the' and words[i] != 'her' and words[i] !=  'his' and words[i] != 'and' and words[i] != 'she':
            return  words[i]
    return words[7]

    ## 使用正则表达式进行分词，并去除标点符号和转换为小写  
    #words = re.findall(r'\b\w+\b', text.lower())  
    ## 去除停用词  
    #words = [word for word in words if word not in STOPWORDS]  
    ## 统计词频  
    #word_counts = collections.Counter(words)  
    ## 返回频率最高的词  
    #return word_counts.most_common(1)[0][0] 

def mainKeywords(dirPath):
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == '.txt':
            print(f'the keywords of {i} is:')
            with open(i, 'r', encoding='utf-8') as fp:
                str1 = fp.read().split(' ')
            b = collections.Counter(str1)
            keywords = sorted(b, key=lambda x: b[x],reverse = True)
            print(judgeit(keywords))

if __name__ == "__main__":
    mainKeywords('/mnt/f/Download/mobile_folder/sharefile')
