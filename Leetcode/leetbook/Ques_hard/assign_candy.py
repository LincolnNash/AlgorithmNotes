"""
题目描述
    一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，
    规则是如果一个孩子的评分比自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果;
    所有孩子至少要有一个糖果。求解最少需要多少个糖果。
"""
import sys
scores = sys.stdin.readline().strip().split(" ")
scores = list(map(int, scores))
candies = [1]*len(scores)
for i in range(1, len(scores)):
    if scores[i] > scores[i-1]:
        candies[i]+=1
for j in range(len(scores)-2, -1, -1):
    if scores[j]>scores[j+1]:
        candies[j] += 1
print(sum(candies))
