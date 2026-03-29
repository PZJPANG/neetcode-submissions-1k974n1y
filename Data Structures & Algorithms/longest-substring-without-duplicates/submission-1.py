class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        best = cur = 0
        l = 0 
        for r in range(len(s)):
            while s[r] in char and l < len(s):
                char.remove(s[l])
                l += 1
            cur = r - l + 1
            best = max(cur, best)
            char.add(s[r])
        return best