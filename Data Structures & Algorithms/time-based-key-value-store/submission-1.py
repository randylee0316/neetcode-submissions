class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.store.get(key, [])) - 1
        values = self.store.get(key, [])
        if values == []:
            return ""
        while l <= r:
            m = (l+r)//2
            if timestamp == values[m][1]:
                return values[m][0]
            elif timestamp < values[m][1]:
                r = m-1
            else:
                l = m+1
        if l == 0:
            return ""
        return values[l-1][0]

        
