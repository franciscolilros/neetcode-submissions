class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = set()
        for i in nums:
            if i in temp:
                return i
            else:
                temp.add(i)
                