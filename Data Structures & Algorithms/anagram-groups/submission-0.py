from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        anagram_map = defaultdict(list)
        for string in strs:
            # Create an array to count occurrences of each lowercase letter a-z
            count = [0] * 26 
            for char in string:
                count[ord(char) - ord('a')] += 1
                
            # Convert mutable list to an immutable tuple to use as a dict key
            anagram_map[tuple(count)].append(string)
            
        return list(anagram_map.values())