class TimeMap:

    """
    yur still not horrendous at binary search

    originally did not realisze to use a b search tho so i need to be more flexible.

    relearned that since i do a floor divide in half (l+r)//2, i must move l = m+1 and r= m rather than r = m-1 and l = m. that requires (l+r+1)//2

    130 ms runtime beats 56%
    """

    def __init__(self):
        self.d = {}

        # store like: key -> key, value -> tup(time stamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        items = self.d[key]
        res = ""
        l, r = 0, len(items)

        while l < r:
            m = (l+r)//2
            item = items[m]
            if item[0] == timestamp: 
                res = item[1]
                break
            elif item[0] > timestamp:
                r = m
            else:
                res = item[1]
                l = m + 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
