import random


class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        else:
            self.m[val] = len(self.l)
            self.l.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.m:
            last_val = self.l.pop()  # get last val
            if val != last_val:
                # Replace removed ele with last ele
                ind = self.m[val]  # get removed index
                self.m[last_val] = ind  # update last_val index
                self.l[ind] = last_val  # update list

            del self.m[val]  # delete val from hashmap
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_ind = random.randint(0, len(self.l) - 1)
        return self.l[random_ind]
