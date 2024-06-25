'''
程序31】
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续
　　　判断第二个字母。
python2 使用 letter = stdin.read(1)  和  stdin.flush()
python3 使用 input
1.程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
2.程序源代码：
'''
letter = input('input a letter:')
while True:
    if letter == 'S':
        print('please input second letter:')
        letter = input('input a letter:')
        if letter == 'a':
            print('Saturday')
            break
        elif letter  == 'u':
            print('Sunday')
            break
        else:
            print('data error')
    elif letter == 'F':
        print('Friday')
        break
    elif letter == 'M':
        print('Monday')
        break
    elif letter == 'T':
        print('please input second letter:')
        letter = input('input a letter:')
        if letter  == 'u':
            print('Tuesday')
            break
        elif letter  == 'h':
            print('Thursday')
            break
        else:
            print('data error')
            # break
    elif letter == 'W':
        print('Wednesday')
        break
    else:
        print('data error')
    letter = input('input a letter:')
