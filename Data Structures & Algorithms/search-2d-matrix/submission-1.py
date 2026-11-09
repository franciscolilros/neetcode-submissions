class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect
        numList = []
        for i in range(len(matrix)):
            numList += matrix[i]
        
        res = bisect.bisect_left(numList, target)

        if res < 0 or res >= len(numList):
            return False
        elif numList[res] == target:
            return True
        return False