class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = sorted(i for i in s)
        temp2 = sorted(i for i in t)
        if temp1 == temp2:
            return True
        else:
            return False