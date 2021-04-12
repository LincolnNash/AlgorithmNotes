"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
import sys

nums = sys.stdin.readline().strip().split(" ")
nums = list(map(int, nums))
target = int(sys.stdin.readline().strip())


# 要求空间复杂度为O(1)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

# 要求时间复杂度为O(n)
hashmap = {}
for i in range(len(nums)):
    # 这里有一个重复数据覆盖问题，后面的重复数据覆盖前面数据的下标
    # 但是在这道题中不影响结果
    hashmap[nums[i]] = i
for j in range(len(nums)):
    res = target - nums[j]
    if res in hashmap and j != hashmap[res]:
        print([j, hashmap[res]])
        break


