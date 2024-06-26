'''
【程序37】
题目：对10个数进行排序
1.程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，
　　　　　　下次类推，即用第二个元素与后8个进行比较，并进行交换。 　　　　　　 
2.程序源代码： 
'''
if __name__ == "__main__":
    N = 10
    # input data
    print('please input ten num:\n')
    l = []
    for i in range(N):
        l.append(int(input('>')))

    # sort ten num
    for i in range(N - 1):
        min_num = i
        for j in range(i + 1,N):
            if l[min_num] > l[j]:
                min_num = j
        l[i],l[min_num] = l[min_num],l[i]
    print('after sorted')
    for i in range(N):
        print(l[i])
                 
