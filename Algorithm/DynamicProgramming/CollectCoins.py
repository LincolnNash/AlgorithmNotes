"""
给你 k 种面值的硬币，面值分别为 c1, c2 ... ck ，每种硬币的数量无限，
再给一个总金额 amount ，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回-1

step1: 确定状态 总金额amount

step2: dp数组的含义 凑除金额为amount的最少硬币

step3：明确选择 导致状态改变的行为本题指可选择的硬币数量

step4：明确baseCase 当amount=0 return 0； 当amount<0 return -1

"""
def colCoins_rec(coins, amount):
    """
    递归解法
    :param coins:
    :param amount:
    :return:
    """
    # base case
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    # 选择
    res = float("inf")
    for coin in coins:
        subproblem = colCoins_rec(coins, amount-coin)
        if subproblem < 0: continue
        res = min(res, 1+colCoins_rec(coins, amount-coin))
    return res

mem = [-1]*15
def colCoins_rec_mem(coins, amount, mem):
    """
    在递归的解法的基础上加上备忘录
    :param coins: 硬币面值
    :param amount: 总金额
    :param mem: 备忘录
    :return: 最少硬币数量
    """
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    if mem[amount] != -1:
        return mem[amount]
    res = float("inf")
    for coin in coins:
        subproblem = colCoins_rec_mem(coins, amount-coin, mem)
        if subproblem < 0: continue
        res = min(res, 1+colCoins_rec_mem(coins, amount-coin, mem))
        mem[amount] = res
    return res

def colCoins_mem(coins, amount):
    """
    自底向上递推出答案
    :param coins:
    :param amount:
    :return:
    """
    mem = [0]*(amount+1)  # mem[i]凑出金额i需要的最少硬币的数量
    for i in range(1, amount+1):
        for coin in coins:
            res = i - coin
            if res >= 0:
                mem[i] = mem[res] + 1
            else:
                continue
    return mem[amount]

##对动态规划的理解
"""
我们画出递归树：
假设目标金额是5，每个节点代表金额。
                   5
                /  ｜   \
             4      3    0
            / \    / \ 
           3   2   2  1
          / \ / \  .......
         2  1 1 0
         .......
把这颗递归树补齐后，叶子节点都变为变为0，那么将0作为base case，迭代的推出目标金额。
也可以将该问题看作求最短路径问题
"""

coins = [1,3,5]
print(colCoins_rec(coins, 11))
print(colCoins_rec_mem(coins, 9, mem))
print(colCoins_mem(coins, 11))
print(colCoins_mem(coins, 9))
