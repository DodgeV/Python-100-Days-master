"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。


"""

def isPalindrome(x: int) -> bool:
    if x <= 0: return x == 0    # 非正数，负数肯定不是回文数，0是回文数
    if x % 10 == 0: return False    # 个位为0肯定不是回文数
    reverse_x = 0       # 反转数
    # 反转x的一半位数
    while x > reverse_x:
        reverse_x *= 10
        reverse_x += x % 10
        x //= 10
        # 如果x为回文数：
        #  x为偶数长度：后半部分反转后和前半部分一致
        #  x为奇数长度：后半部分反转后去掉最低位与x一致
    return reverse_x == x or reverse_x // 10 == x

if __name__ == "__main__":
    num = eval(input('input a palindrome number and return T/F:'))
    print(isPalindrome(num))
