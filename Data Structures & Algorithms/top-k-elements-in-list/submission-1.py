from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count occurrences
        counts = Counter(nums)

        # Step 2: Push items onto the heap with negative frequencies
        max_heap = []
        for item, freq in counts.items():
            heapq.heappush(max_heap, (-freq, item))
        sol = []
        for i in range(k):
            sol.append(heapq.heappop(max_heap)[1])
        return sol