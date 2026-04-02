from random import randint

class RandomizedSet:

    def __init__(self):
        '''
        map -> num: idx

        remove:
        -> get idx of removed item -> put last item val there -> update map
        -> pop from list -> del from map
        '''
        self.numToIdx = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        notPresent = val not in self.numToIdx

        if notPresent:
            self.numToIdx[val] = len(self.nums)
            self.nums.append(val)

        return notPresent
        

    def remove(self, val: int) -> bool:
        canRemove = val in self.numToIdx

        if canRemove:
            idx = self.numToIdx[val]
            lastVal = self.nums[-1]

            self.nums[idx] = lastVal
            self.numToIdx[lastVal] = idx

            self.nums.pop()
            del self.numToIdx[val]
            
        return canRemove

    def getRandom(self) -> int:
        randIdx = randint(0, len(self.nums) - 1)

        return self.nums[randIdx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()