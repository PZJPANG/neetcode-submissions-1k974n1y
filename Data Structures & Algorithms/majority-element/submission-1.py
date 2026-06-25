class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1
            if num_to_freq[num] > n / 2:
                return num