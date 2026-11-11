class TimeMap:
    def __init__(self):
        
        self.dicc = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dicc[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        import bisect
        index = bisect.bisect_left(self.dicc[key], timestamp, key=lambda a:a[0])
        if len(self.dicc[key]) == 0:
            return ""
        elif index >= len(self.dicc[key]):
            index -= 1
        elif self.dicc[key][index][0] != timestamp:
            if index == 0:
                return ""
            else:
                index -= 1
        return self.dicc[key][index][1]