"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
    Input: s = ""
    Output: 0

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""
s = "pwwkew"
left = 0
right = 0
window = set()
ans = 0
bestAns = 0
while right < len(s):
    if s[right] not in window:
        window.add(s[right])
        ans += 1
        right += 1
    else:
        if bestAns < ans:
            bestAns = ans
        while left < right:
            window.remove(s[left])
            ans -= 1
            if s[left] == s[right]:
                left += 1
                break
            left += 1
print(max(bestAns, ans))





