class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for char in s1:
            count[char] = 1 + count.get(char, 0) # {'a': 1, 'b': 1, 'c': 1}

        l = 0
        window_size = len(s1)
        window = {} 
        for r in range(len(s2)): 
            # Add the new element to the window
            window[s2[r]] = window.get(s2[r], 0) + 1 # {l: 1, e}

            # Shrink the window size to ensure validity of window
            if (r - l + 1) > window_size: 
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            
            if window == count:
                return True
        
        return False
            
            

