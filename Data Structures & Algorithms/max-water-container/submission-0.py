class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(heights)-1

        res = min(heights[pointer1],heights[pointer2])* (pointer2-pointer1)

        while pointer1 < pointer2:
            area = min(heights[pointer1],heights[pointer2])* (pointer2-pointer1)
            if min(heights[pointer1],heights[pointer2])* (pointer2-pointer1) > res:
                res = area
            
            if heights[pointer1] <= heights[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return res