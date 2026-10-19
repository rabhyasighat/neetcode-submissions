class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for n in nums:
            key = n
            if key not in groups:
                groups[key] = 1
            else:
                groups[key] += 1
            
        new_list = sorted(groups.items(), key=lambda pair: pair[1], reverse = True)

        final = []
        for i in new_list[:k]:
            final.append(i[0])

        return final