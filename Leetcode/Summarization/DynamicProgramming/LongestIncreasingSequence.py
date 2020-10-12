"""
300. Longest Increasing Subsequence
    Given an unsorted array of integers, find the length of longest increasing subsequence.

    Example:

    Input: [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    Note:

        There may be more than one LIS combination, it is only necessary for you to return the length.
        Your algorithm should run in O(n2) complexity.

    Follow up: Could you improve it to O(n log n) time complexity?

    总结：
        动态规划就像填dp数组的游戏，要明确以下几点：
        1、dp数组的含义（状态）
        2、明确dp数组的初始状态（base case）
        3、递推dp数组的规则（状态转移方程）
"""
def lengthOfLIS(nums):
    dp = [0]*len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        length = float("-inf")
        for j in range(i):
            if nums[i] > nums[j]:
                length = max(length, dp[j]+1)
                dp[i] = length
    return max(dp)

nums=[1,4,2,7,8,3]
dp, ans = lengthOfLIS(nums)

