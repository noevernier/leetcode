import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.buffer = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.buffer.append(val)
        self.dict[val] = self.size
        self.size += 1

        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            val_index = self.dict.pop(val)
           
            if val_index == self.size-1:
                self.buffer.pop(self.size - 1)
                self.size -= 1
                return True
            last_val = self.buffer[self.size - 1]
            self.buffer[val_index], self.buffer[self.size - 1] = last_val, self.buffer[val_index]
            self.dict[last_val] = val_index
            self.buffer.pop(self.size - 1)
            self.size -= 1
            return True
        return False        

    def getRandom(self) -> int:
        return random.choice(self.buffer)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()