class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_dict = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))
            sorted_dict[s_sorted].append(s)
        
        return list(sorted_dict.values())

        