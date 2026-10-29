class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ","")
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()
        pointer1 = 0
        pointer2 = len(s)-1
        while pointer1 < len(s)//2:
            if s[pointer1] != s[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True