"""
问题描述：
    给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两 个属性。
    其中第 i 个物品的重量为 wt[i] ，价值为 val[i] ，现在让你用 这个背包装物品，最多能装的价值是多少?
"""
N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
dp = [[0]*(W+1) for i in range(N+1)]

# 定义好我们的dp数组含义，我们就来开始我们的填空格游戏
for w in range(1, W+1):
    for n in range(1, N+1):
        if w >= wt[n-1]:
            # 装进去
            a = val[n-1]+dp[n-1][w-wt[n-1]]
            # 不装进去
            b = dp[n-1][w]
            dp[n][w] = max(a, b)
        else:
            dp[n][w] = dp[n-1][w]
print(dp[N][W])

