class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        values = self.hash.get(key, [])
        right = len(values) - 1
        result = ""
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle +1
            else:
                right = middle -1
        return result

