class TimeMap:

    def __init__(self):
        self.keyToTime = defaultdict(list) # key -> time
        self.timeToVal = {} # key + time -> value

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToTime[key].append(timestamp)
        self.timeToVal[key + str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.keyToTime.get(key)
        if not timestamps or timestamps[0] > timestamp:
            return ""
        if timestamps[-1] <= timestamp:
            return self.timeToVal[key + str(timestamps[-1])]
        
        l, r = 0, len(timestamps) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamps[m] == timestamp:
                return self.timeToVal[key + str(timestamps[m])]
            elif timestamps[m] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return self.timeToVal[key + str(timestamps[r])]
