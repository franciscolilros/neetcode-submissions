class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l = 0
        r = len(nums) - 1
        

        while nums[l] != nums[r] - 1:
            temp = nums[(r + l) // 2]

            if nums[r] < temp:
                l = (r + l) // 2
            elif nums[l] > temp:
                r = (r + l) // 2
            else:
                res = 0
                break
            
            if l == r - 1:
                if nums[l] < nums[r]:
                    res = l
                    break
                else:
                    res = r
                    break

                    
        if l == r - 1:
            if nums[l] < nums[r]:
                res = l
            else:
                res = r
        print(res)

        import bisect
        listFin = nums[res:] + nums[:res]
        print(listFin)
        numFin = bisect.bisect_left(listFin, target)

        if numFin < 0 or numFin >= len(nums):
            return -1
        if listFin[numFin] == target:
            return (numFin + res) % len(nums)
        else:
            return -1