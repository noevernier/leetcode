class TimeMap:

    def __init__(self):
        self.dict = {}
        self.dict_key_list = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].update({timestamp: value})
            self.dict_key_list[key].append(timestamp)
        else:
            self.dict[key] = {timestamp: value}
            self.dict_key_list[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dict_key_list:
            return ""
        timestamps = self.dict_key_list[key]

        n = len(self.dict[key])
        l = 0
        r = n - 1

        res = l

        if n==0:
            return ""
        
        if timestamps[0] > timestamp:
            return ""

        while l <= r:
            m = (l+r) // 2
            if timestamps[m] <= timestamp:
                l = m+1
                res = m
            else:
                r = m-1
        return self.dict[key][timestamps[res]]