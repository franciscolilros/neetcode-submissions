class Solution:
    def search(self, nums: List[int], target: int) -> int:
        div = int(math.log2(len(nums))) + 1
        print(div)
        lower = 0
        upper = len(nums)
        temp = len(nums) // 2
        for _ in range(div):
            if nums[temp] == target:
                return temp
            elif nums[temp] > target:
                upper = temp
                temp = (temp + lower) // 2
            else:
                lower = temp
                temp = (temp + upper) // 2
        
        if nums[temp] == target:
            return temp
        return -1
