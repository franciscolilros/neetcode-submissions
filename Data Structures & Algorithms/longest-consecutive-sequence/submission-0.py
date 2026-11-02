class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_cont = 0
        for i in numSet:
            k = i
            cont = 1
            if not(k-1 in numSet):
                while k + 1 in numSet:
                    k += 1
                    cont += 1
            if max_cont < cont:
                max_cont = cont
        return max_cont