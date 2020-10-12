"""
三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
def ThreeSum(nums):
    # 先排序
    nums.sort()
    # 数组元素都大于0则无解
    if nums[0] > 0:
        return []
    ans = []
    # 遍历组合
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        j = i+1
        k = len(nums) - 1

        while(j < k):
            if nums[j] + nums[k] == target:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                while(nums[j] == nums[j-1] and j < k):
                    j += 1
            elif nums[j] + nums[k] < target:
                j += 1
                while (nums[j] == nums[j-1] and j < k):
                    j += 1
            else:
                k -= 1
                while (nums[k] == nums[k+1] and j < k):
                    k -= 1
    return ans

a = [-1, 0, 1, 2, -1, -4]
ans = ThreeSum(a)
print(ans)

a = [0,0,0,0,0,0]
ans = ThreeSum(a)
print(ans)

