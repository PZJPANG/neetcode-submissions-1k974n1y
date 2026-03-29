class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            k = (l + r) // 2
            time = 0
            for pile in piles:
                time += - (-(pile) // k)
            if time <= h:
                r = k - 1
                ans = k 
            else:
                l = k + 1
        return ans