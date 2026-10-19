class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a set cannot have duplicates 
        seen = set() 
        for n in nums:
            # if number n is already present in seen set()
            if n in seen:
                return True
            seen.add(n)
        return False

        