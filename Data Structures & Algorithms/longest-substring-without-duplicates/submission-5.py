class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        seen = [s[0]]
        longest = 0
        l = r = 0
        while r < len(s):
            while s[r] in seen:
                seen.pop(0)
                l += 1                
            seen.append(s[r])
            r += 1
            longest = max(longest, r - l + 1)
        return longest