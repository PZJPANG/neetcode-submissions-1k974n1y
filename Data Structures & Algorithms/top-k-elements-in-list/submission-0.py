class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = 1 + num_to_freq.get(num, 0)
        
        array = []
        for num in num_to_freq:
            array.append((num_to_freq[num], num))
        array.sort()

        ans, n = [], 0
        while n < k:
            ans.append(array.pop()[1])
            n += 1
        return ans