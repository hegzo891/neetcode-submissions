from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for i in strs:
            dictionary[tuple(sorted(i))].append(i)
        return list(dictionary.values())