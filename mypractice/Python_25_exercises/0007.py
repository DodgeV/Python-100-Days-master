'''
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os, re

def mainKeywords(dirPath):
    blank, comments, codelines, totalines, count, temp = 0, 0, 0, 0, 0, 0
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == '.py':
            file_path = os.path.join(dirPath, i)
            print(f">Processing file: {file_path}")  
            with open(file_path, 'r', encoding='utf-8') as fp:
                multiline_comment = False  
                for line in fp:  
                    totalines += 1  
                    if multiline_comment:  
                        if '"""' in line or "'''" in line:  
                            if line.strip().endswith('"""') or line.strip().endswith("'''"):  
                                multiline_comment = False  
                            comments += 1  
                    elif line.strip().startswith('#'):  
                        comments += 1  
                    elif '"""' in line or "'''" in line:  
                        if line.strip().startswith('"""') or line.strip().startswith("'''"):  
                            multiline_comment = True  
                            comments += 1  
                    elif line.strip():  
                        codelines += 1  
                    else:  
                        blank += 1  

    print('The total number of lines is : ' + str(totalines))  
    print('The number of comments is : ' + str(comments))  
    print('The number of code lines is : ' + str(codelines))  
    print('The number of blank lines is : ' + str(blank))

if __name__ == "__main__":
    mainKeywords('.')

