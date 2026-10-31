class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [0] * k
        dicc = defaultdict(int)
        for i in nums:
            dicc[i] += 1
        
        temp = [(i, dicc[i]) for i in list(dicc.keys())]

        temp = sorted(temp,key= lambda x: x[1])
        for i in range(-1, -k-1, -1):
            res.append(temp[i][0])


        return res