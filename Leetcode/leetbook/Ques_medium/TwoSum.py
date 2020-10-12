"""
给定一个数组nums和target，在nums里找到和为target的两个数。并且返回这两个数的下标

注意：数组中的元素不能被使用两次

示例：
    input: nums=[2, 7, 11, 15], target= 9
    output: [0, 1] (因为 nums[0]+nums[1])
"""

def TwoSum(nums, target):
    dic = {}
    ans = []
    # 记录每个元素的另一半
    for i in range(len(nums)):
        dic[target - nums[i]] = i
    # 寻找非自身的另一半
    for i in range(len(nums)):
        if nums[i] in dic and i != dic[nums[i]]:
            ans.append(i)
            ans.append(dic[nums[i]])
            break
    return ans

a = [ 11, 15, 2, 7]
print(TwoSum(a, 9))

# def TwoSum(nums, target):
#     ans = []
#     nums.sort()
#     i = 0
#     j = len(nums)-1
#     while i<j:
#         if nums[i] + nums[j] == target:
#             ans.append(i)
#             ans.append(j)
#             j -= 1
#         elif nums[i] + nums[j] < target:
#             i += 1
#         else:
#             j -= 1
#     return ans
#
# a = [ 11, 15, 2, 7]
# print(TwoSum(a, 9))

