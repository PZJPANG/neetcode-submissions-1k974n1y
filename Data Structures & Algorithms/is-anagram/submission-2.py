class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char_to_freq = defaultdict(int)
        for char in s:
            s_char_to_freq[char] += 1
        for char in t:
            if char in s_char_to_freq:
                if s_char_to_freq[char] > 0:
                    s_char_to_freq[char] -= 1
                else:
                    return False
            else:
                return False
        return True