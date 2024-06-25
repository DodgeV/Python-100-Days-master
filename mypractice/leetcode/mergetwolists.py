"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""

def mergeTwoLists(a,b):
    if not a:
        for i in b:
            addlist.append(i)
        return addlist
    if not b: 
        for i in a:
            addlist.append(i)
        return addlist
    if a[0] <= b[0]:  # 递归调用
        addlist.append(a[0])
        a.remove(a[0])
        return mergeTwoLists(a,b)
    else:
        addlist.append(b[0])
        b.remove(b[0])
        return mergeTwoLists(a,b)

# def mergeTwoLists(list1, list2):
#     for a, b in zip(list1, list2):
#         if eval(a) > eval(b):
#             list1.insert(list1.index(a), b)
#         else:
#             list2.insert(list2.index(b), a)
#     return list1,list2


if __name__ == "__main__":
    addlist = []
    list1 = [i for i in input("input a list1:").split()]
    list2 = [i for i in input("input a list2:").split()]
    print(mergeTwoLists(list1, list2))
