class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for s in strs:

            key= "".join(sorted(s))
            if key in group:
                group[key].append(s)
            elif key not in group:
                group[key]=[s]

        return list(group.values())

            