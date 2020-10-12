n = 3
coins = [1, 2, 5]
amount = 5

dp = [[0]*(amount+1) for i in range(n+1)]
for i in range(4):
    dp[i][0] = 1

for i in range(1,amount+1): # amount
    for j in range(1, n+1): # coin
        if i >= coins[j-1]:
            # 加入
            a = dp[j][i-coins[j-1]]
            # 不加入
            b = dp[j-1][i]
            dp[j][i] = a+b
        else:
            dp[j][i] = dp[j-1][i]
print(dp[n][amount])

