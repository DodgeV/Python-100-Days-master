"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""

def twoSum(nums, target):
    for i in range(len(nums)):
        # 计算需要找到的下一个目标数字
        res = target-nums[i]
            # 遍历剩下的元素，查找是否存在该数字
        if res in nums[i+1:]:
            # 若存在，返回答案。这里由于是两数之和，可采用.index()方法
            # 获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
            print([i, nums[i+1:].index(res)+i+1])


if __name__ == "__main__":
    nums = [eval(i) for i in input('input a num list:').split(' ')]
    target = eval(input('input a sum num:'))
    twoSum(nums, target)

