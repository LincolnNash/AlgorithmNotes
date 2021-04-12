"""
动态规划要素：
            重叠子问题、状态转移方程、最优子结构
            本节使用斐波那契数列来介绍重叠子问题和状态转移方程
"""


def fib_rec(n):
    """
    递归方法求斐波那契数列：
        递归树
                    20
                 /     \
                18      19
              /  \     /  \
            16   17   17  18
        从递归数我们可以看到17、18节点被重复计算（称为重叠子问题）。所以递归算法的时间复杂度为递归树的节点树O(2^n)
        空间复杂度主要是是递归树的调用栈。如何解决重叠子问题呢？
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib_rec(n-2)+fib_rec(n-1)



mem1 = [0]*10
def fib_rec_mem(mem, n):
    """
    使用备忘录mem来记录每个节点的值，解决了重叠子问题，需要时直接从mem中获取不用重复计算，属于空间换时间的方法。
    该方法使用置顶向下的方法来计算斐波那契值，但是仍然属于递归方法，存在调用栈。
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    if mem[n]!=0:
        return mem[n]
    mem[n] = fib_rec_mem(mem,n-2)+fib_rec_mem(mem,n-1)
    return mem[n]



mem2 = [0]*10
def fib_mem(mem, n):
    """
    该方法根据状态转移方程至底向上的推导斐波数列
    """
    mem[1] = 1
    mem[2] = 1
    for i in range(3,n+1):
        mem[i] = mem[i-2] + mem[i-1]
    return mem[n]

def fib(n):
    """
    从斐波那契数列的公式我们知道，当前节点的值只与前两个节点相关，所以我们只用维护前两个变量。
    """
    p1 = 1
    p2 = 1
    for i in range(n-2):
        cur = p1+p2
        p1 = p2
        p2 = cur
    return cur

# 测试
print(fib_rec(5))
print(fib_rec_mem(mem1, 5))
print((fib_mem(mem2, 5)))
print(fib(5))



