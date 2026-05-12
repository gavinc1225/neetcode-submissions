class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sortedWord = ''.join(sorted(s))
            result[sortedWord].append(s)
        
        return list(result.values())