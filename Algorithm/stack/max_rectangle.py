"""
最大矩形：
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""
import sys
ipt = sys.stdin.readline().strip().split(" ")
ipt = list(map(int, ipt))
print(ipt)
# 添加哨兵
ipt = [0]+ipt+[0]
# 单调栈
stack = [0]
ans = 0
for i in range(1, len(ipt)):
    # 当前矩形的高小于栈顶元素开始计算以栈顶元素为高的矩形面积
    while ipt[i] < ipt[stack[-1]]:
        curr_height = ipt[stack.pop()]
        width = i - stack[-1] - 1
        ans = max(ans, curr_height*width)
    # 当前矩形的的高大于栈顶元素则压入栈
    stack.append(i)
print(ans)
