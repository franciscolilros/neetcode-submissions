class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        dicc = defaultdict(int)
        res = ""
        min_len = float("inf")
        for i in t:
            dicc[i] += 1
        
        curr = defaultdict(int)
        for r in range(len(s)):
            temp = s[r]
            curr[temp] += 1
            while l < r and curr[s[l]] > dicc[s[l]]:
                curr[s[l]] -= 1
                l += 1
            k = True
            for i in dicc.keys():
                if curr[i] < dicc[i]:
                    k = False
            
            if k and ((r - l + 1) < min_len):
                res = s[l:r+1]
                min_len = r-l+1

        return res