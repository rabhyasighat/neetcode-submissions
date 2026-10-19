class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        s2 = list(t)
        # sorting using sorted and storing in an array  
        a = sorted(s1)
        b = sorted(s2)
        # bring the sorted array back to string using join
        x = "".join(a)
        y = "".join(b)
        if x == y:
            return True
        else:
            return False