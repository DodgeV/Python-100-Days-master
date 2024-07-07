import string

def coding(name):
    # 使用with语句确保文件正确关闭
    with open(name, "rt", encoding='utf-8') as t:
        txt = t.read()

    # 创建加密字典，直接向前移动16位（13+3）
    # 注意：这里使用string.ascii_lowercase和string.ascii_uppercase来简化
    shift = 16
    d = {c: chr((ord(c) - ord('A' if c.isupper() else 'a') + shift) % 26 + ord('A' if c.isupper() else 'a')) for c in string.ascii_letters}

    # 使用字典映射或保持原字符（如果不在字典中）
    encrypted_txt = ''.join(d.get(c, c) for c in txt)

    # 把加密后结果打印出来
    print(encrypted_txt)

# 调用函数
coding('example.txt')  # 替换为你的文件名
