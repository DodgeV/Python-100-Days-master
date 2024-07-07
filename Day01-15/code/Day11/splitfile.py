import pickle

def write_file(data, filename, mode):
    """根据给定的数据和模式（二进制或文本）写入文件"""
    if mode == 'wb':
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    elif mode == 'wt':
        with open(filename, 'wt', encoding='utf-8') as f:
            f.writelines(data)

def split_and_save(filename, choice):
    """从文件中读取数据，根据分隔符分割，并根据选择保存到不同文件"""
    speak = []
    say = []
    count = 1
    try:
        with open(filename, 'r', encoding='utf-8') as t:
            for line in t:
                if line.startswith('===='):
                    write_file((speak, say), f'boy_{count}.txt', choice) if choice.startswith('0') else None
                    write_file((say, speak), f'girl_{count}.txt', choice) if choice.startswith('0') else None
                    speak, say = [], []
                    count += 1
                else:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        speaker, content = parts
                        if speaker.strip() == 'boy':
                            speak.append(content.strip() + '\n')
                        elif speaker.strip() == 'girl':
                            say.append(content.strip() + '\n')
            # 处理最后一部分数据
            if speak or say:
                write_file((speak, say), f'boy_{count}.txt', choice) if choice.startswith('0') else None
                write_file((say, speak), f'girl_{count}.txt', choice) if choice.startswith('0') else None
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 使用示例
choice = input('0b/0d:')  # 用户输入二进制或文本模式
split_and_save('record.txt', choice)
