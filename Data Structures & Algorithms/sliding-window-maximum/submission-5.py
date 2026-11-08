class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNum = -100000
        temp = defaultdict(int)
        for i in range(k):
            maxNum = max(maxNum, nums[i])
            temp[nums[i]] += 1
        
        res = [maxNum]
        
        l = 0
        for r in range(k, len(nums)):
            if temp[nums[l]] == 1:
                del temp[nums[l]]
            else:
                temp[nums[l]] -= 1
            l += 1
            temp[nums[r]] += 1
            if nums[r] < maxNum:
                maxNum = max(set(temp.keys()))
            else:
                maxNum = nums[r]
            res.append(maxNum)
        return res