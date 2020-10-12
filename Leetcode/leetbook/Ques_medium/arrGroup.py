"""
字母异位词分组

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
    所有输入均为小写字母。
    不考虑答案输出的顺序。
"""
# 排序+hash表法
def groupAnagrams(arr):
    ans = {}
    for str in arr:
        key = tuple(sorted(str))
        if key not in ans:
            ans[key] = [str]
        else:
            ans[key].append(str)
    return list(ans.values())