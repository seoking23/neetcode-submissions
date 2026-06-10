class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #forward arr
        forward = [0] * len(nums)
        forward[0] = nums[0]
        i = 1
        while i < len(nums):
            forward[i] = forward[i-1] * nums[i]
            i += 1
        #backward arr
        backward = [0] * len(nums)
        backward[len(nums)-1] = nums[len(nums)-1]
        i = len(nums) - 2
        while i >= 0:
            backward[i] = backward[i + 1] * nums[i]
            i -= 1
        
        sol = [0] * len(nums)
        sol[0] = backward[1]
        i = 1
        while i < len(nums) - 1:
            sol[i] = forward[i-1] * backward[i+1]
            i += 1
        sol[i] = forward[i-1]

        return sol