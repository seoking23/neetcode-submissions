class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        n = len(height)
        if n == 0:
            return 0
        for i in range(n):
            while stack and height[i] >= height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    h = min(right, left) - bottom
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res