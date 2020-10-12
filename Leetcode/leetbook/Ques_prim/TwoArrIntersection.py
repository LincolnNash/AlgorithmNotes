"""
两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：
    输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
    我们可以不考虑输出结果的顺序。
进阶：
    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
# hash表法
def intersect1(arr1, arr2):
    '''
    空间复杂度：o(m+n)
    时间复杂度: o(n)
    '''
    dic1 = {}
    dic2 = {}
    ans = []
    for num in arr1:
        if num not in dic1:
            dic1[num] = 1
        else:
            dic1[num] += 1
    for num in arr2:
        if num not in dic2:
            dic2[num] = 1
        else:
            dic2[num] += 1
    for key in dic1:
        if key in dic2:
            times = min(dic1[key], dic2[key])
            ans.extend([dic1[num]]*times)
    return ans


# 排序+指针法
def intersect2(nums1, nums2):
    """
    时间复杂度：o( m*log(m) + n*log(n) + min(o(m), o(n) )
    空间复杂度：O(min(n, m))
    """
    nums1.sort()
    nums2.sort()
    ans = []
    p1 = 0
    p2 = 0
    while(p1 < len(nums1) and p2 < len(nums2)):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            ans.append(nums1[p1])
            p1 += 1
            p2 += 1
    return ans
