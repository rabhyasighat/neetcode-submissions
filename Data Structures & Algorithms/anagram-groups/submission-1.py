class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:       
        final = {}
        for s in strs:
            key=''.join(sorted(s))
            if key not in final:
                final[key]=[]
            final[key].append(s)

        return list(final.values())
            