class TimeMap:

    def __init__(self):
        self.tm_list = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.tm_list:
            self.tm_list[key] = [[value, timestamp]]
        else:
            self.tm_list[key].append([value, timestamp])
        return None
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.tm_list or  timestamp < self.tm_list[key][0][1]:
            return ""
        if timestamp >= self.tm_list[key][-1][1]:
            return self.tm_list[key][-1][0]
        l = 0
        r = len(self.tm_list[key])-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if self.tm_list[key][mid][1] <= timestamp:
                l = mid+1
            else:
                r = mid-1
        if l == 0:
            return None
        return self.tm_list[key][l-1][0]
    
def get_vals(tm_funcs, tm_vals):
    res = []
    for i in range(len(tm_funcs)):
        if tm_funcs[i] == "TimeMap":
            tm = TimeMap()
            res.append(None)
        elif tm_funcs[i] == "set":
            res.append(tm.set(tm_vals[i][0], tm_vals[i][1], tm_vals[i][2]))
        elif tm_funcs[i] == "get":
            res.append(tm.get(tm_vals[i][0], tm_vals[i][1]))
    return res



tm_funcs = ["TimeMap", "set", "get", "get", "set", "get", "get"]
tm_vals = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]


#tm_funcs = ["TimeMap","set","set","get","get","get","get","get"]
#tm_vals = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]


#tm_funcs = ["TimeMap","set","set","get","set","get","get"]
#tm_vals = [[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]

print(get_vals(tm_funcs, tm_vals))




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)