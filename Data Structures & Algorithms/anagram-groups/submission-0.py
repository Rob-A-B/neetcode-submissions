class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input strs : array of integers
        #output: return sublistts of anagram
        groups=defaultdict(list)

        for s in strs:
            key=tuple(sorted(s))
            groups[key].append(s)

        return list(groups.values())
