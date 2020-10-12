
"""
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S
which will contain all the characters in T in complexity O(n).

Example:
    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"

Note:
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
S = "ADOBECODEBANC"
T = "ABC"

needs = {}
window = {}
for c in T:
    if c not in needs:
        needs[c] = 1
    else:
        needs[c] += 1

left = 0
right = 0
valid = 0
ans = S

while right<len(S):
    #  新增字符
    new_char = S[right]
    if new_char in needs:
        if new_char not in window:
            window[new_char] = 1
            if window[new_char] == needs[new_char]:
                valid += 1
        else:
            window[new_char] += 1
            if window[new_char] == needs[new_char]:
                valid += 1

    # 如果valid的大小和需要字符数量相同则移动left
    while valid == len(needs):
        if ans == "":
            ans = S
        if S[left] in needs:
            window[S[left]] -= 1
            if window[S[left]] < needs[S[left]]:
                valid -= 1
                if right-left+1 < len(ans):
                    ans = S[left:right+1]
                left += 1
                break
        left += 1
    right += 1
print(ans)


