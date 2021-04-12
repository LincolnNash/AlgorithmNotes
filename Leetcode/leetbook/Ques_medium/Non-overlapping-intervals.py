"""
无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:
    可以认为区间的终点总是大于它的起点。
    区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:
输入: [[1,2], [2,3], [3,4], [1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals)<=1:
            return 0
        intervals.sort(key=lambda x: x[-1])
        left = float("-inf")
        ans = 0
        for i in intervals:
            if i[0] >= left:
                left = i[1]
                continue
            ans+=1
        return ans

s = Solution()
ans = s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
print(ans)

