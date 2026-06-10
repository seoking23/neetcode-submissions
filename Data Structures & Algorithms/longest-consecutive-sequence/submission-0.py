class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLength = 0
        for num in nums:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                maxLength = max(length, maxLength)
            
        return maxLength
