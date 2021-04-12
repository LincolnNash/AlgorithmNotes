"""
题目描述
有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。每个孩子只能吃 最多一个饼干，
且只有饼干的大小大于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩 子可以吃饱。
Input: [1,2], [1,2,3] 分别代表孩子的饥饿度和饼干的大小。
Output: 2 输出最多有多少孩子可以吃饱的数量。
"""
import sys
hunger = sys.stdin.readline().strip().split(" ")
hunger = list(map(int, hunger))
cookies = sys.stdin.readline().strip().split(" ")
cookies = list(map(int, cookies))
hunger.sort()
cookies.sort()
i = 0
j = 0
while i < len(hunger) and j < len(cookies):
    if hunger[i] <= cookies[j]:
        i += 1
    j += 1
print(i)


