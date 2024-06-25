'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
1.程序分析：谭浩强的书中答案有问题。　　　　　　
2.程序源代码：
'''
def inp(numbers):
    for i in range(10):
        numbers.append(int(input('input a number:')))

p = 0

def max_min(array):
    max_num = min_num = 0
    for i in range(1,len(array) - 1):
        p = i
        if array[p] > array[max_num] : max_num = p
        elif array[p] < array[min_num] : min_num = p
    k = max_num
    l = min_num
    array[0],array[l] = array[l],array[0]
    array[9],array[k] = array[k],array[9]

if __name__ == '__main__':
    array = []
    inp(array)
    max_min(array)
    print(array)
