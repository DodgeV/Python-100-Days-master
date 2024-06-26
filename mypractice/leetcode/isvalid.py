"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""
def isValid(s):
    dic = {'(':')','{':'}','[':']','?':'?'}
    stack = ['?']
    for c in s:
        if c in dic:stack.append(c)
        elif dic[stack.pop()] != c: return False
    return len(stack) == 1
    

if __name__ == "__main__":
    mystr = input('input  a str:')
    print(isValid(mystr))
