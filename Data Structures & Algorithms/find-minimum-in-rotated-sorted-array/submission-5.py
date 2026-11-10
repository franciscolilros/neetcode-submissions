class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1


        while nums[l] != nums[r] - 1:
            temp = nums[(r + l) // 2]

            if nums[r] < temp:
                l = (r + l) // 2
            elif nums[l] > temp:
                r = (r + l) // 2
            else:
                return nums[0]
            
            if l == r - 1:
                if nums[l] < nums[r]:
                    return nums[l]
                else:
                    return nums[r]

                    
        if l == r - 1:
                if nums[l] < nums[r]:
                    return nums[l]
                else:
                    return nums[r]