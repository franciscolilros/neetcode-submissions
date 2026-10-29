class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) -1
        while pointer1 < len(numbers) - 1:

            if numbers[pointer1] + numbers[pointer2] == target:
                return [pointer1+1, pointer2+1]
            elif pointer2 == pointer1+1 or numbers[pointer1] + numbers[pointer2] < target:
                pointer1 += 1
                pointer2 = len(numbers) - 1
            else:
                pointer2 -= 1
            
            
            
        return 0