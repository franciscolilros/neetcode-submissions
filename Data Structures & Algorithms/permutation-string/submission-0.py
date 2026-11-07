class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicc = defaultdict(int)
        for i in s1:
            dicc[i] += 1
        
        l = 0
        curr = defaultdict(int)
        for r in range(len(s2)):
            curr[s2[r]] += 1
            while curr[s2[r]] > dicc[s2[r]]:
                curr[s2[l]] -= 1
                l += 1
            if curr[s2[r]] == dicc[s2[r]]:
                temp = True
                for j in dicc.keys():
                    if dicc[j] != curr[j]:
                        temp = False
                if temp:
                    return True
        return False