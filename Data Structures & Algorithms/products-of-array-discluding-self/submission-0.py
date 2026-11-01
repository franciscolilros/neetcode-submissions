class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        ac = 1
        cont_null = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res = [0] * len(nums)
                cont_null += 1
                pos = i
            else:
                ac *= nums[i]

        if cont_null >= 2:
            return res
        elif cont_null == 1:
            res[pos] = ac
            return res
        else:
            for i in range(len(nums)):
                res[i] = ac // nums[i]
            return res