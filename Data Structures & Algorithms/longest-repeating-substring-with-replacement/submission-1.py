from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of right letter, keep track of left different letter
        count = defaultdict(int)
        l = maxf = res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(count[s[r]], maxf)
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res 