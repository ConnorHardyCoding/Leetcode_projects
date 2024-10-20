class TimeMap:

    def __init__(self):
        self.dict = {}
        self.dict_list = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict.keys():
            self.dict[key] = [(timestamp, value)]
            self.dict_list[key] = [timestamp]
        else:
            self.dict[key].append((timestamp, value))
            self.dict_list[key].append(timestamp)
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict.keys():
            return ""
        if timestamp < sorted(self.dict_list[key])[0]:
            return ""
        self.dict[key] = sorted(self.dict[key])
        if timestamp not in self.dict_list[key]:
            self.dict_list[key].append(timestamp)
            self.dict_list[key] = sorted(self.dict_list[key])
            target_index = self.dict_list[key].index(timestamp) -1
            self.dict_list[key].remove(timestamp)
            return self.dict[key][target_index][1]
        else:
            target_index = self.dict_list[key].index(timestamp)
            return self.dict[key][target_index][1]
        


            
            

tm = TimeMap()

tm.set("foo", "bar", 1)
print(tm.get("foo", 3))
tm.set("foo", "bar2", 4)
print(tm.get("foo", 5))

