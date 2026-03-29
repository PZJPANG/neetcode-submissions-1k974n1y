class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        char_to_freq = {}
        for char in s:
            char_to_freq[char] = char_to_freq.get(char, 0) + 1
        for char in t:
            if char in char_to_freq:
                if char_to_freq[char] > 0:
                    char_to_freq[char] -= 1
                else: 
                    return False
            else:
                return False
        return True

        