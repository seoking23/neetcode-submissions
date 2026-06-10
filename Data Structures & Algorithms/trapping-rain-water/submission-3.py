class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            rightMax[j] = max(rightMax[j+1], height[j])
        sol = 0
        for k in range(n):
            sol += min(leftMax[k], rightMax[k]) - height[k]
        return sol