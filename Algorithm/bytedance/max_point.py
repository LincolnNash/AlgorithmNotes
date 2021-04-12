# https://www.nowcoder.com/test/question/done?tid=42692189&qid=141057
'''
思路：
    先在一个维度上排逆序，然后在另一个维度上大于它前面的一个点就行了（这样就保证了不存在两个维度上都大于当前点的点存在）
'''
import sys
n = int(sys.stdin.readline().strip())
points = []

for i in range(n):
    s = sys.stdin.readline().strip().split(' ')
    point = tuple(int(c) for c in s)
    points.append(point)
points.sort(key=lambda p:p[0], reverse=True)

ans = [points[0]]
for i in range(1, len(points)):
    if points[i][1]>ans[-1][1]:
        ans.append(points[i])
ans.sort(key=lambda p:p[0])
for i in range(len(ans)):
    print(ans[i][0],ans[i][1])