class MyHashSet:

    def __init__(self):
        self.li=[[] for i in range(10)]

        

    def add(self, key: int) -> None:
        bucket=key%len(self.li)
        if key not in self.li[bucket]:
            self.li[bucket].append(key)
            return None
        else:
            return 


        

    def remove(self, key: int) -> None:
        bucket=key%len(self.li)
        if key not in self.li[bucket]:
            return
        else:
            self.li[bucket].remove(key)
            return None
        

    def contains(self, key: int) -> bool:
        bucket=key%len(self.li)
        if key in self.li[bucket]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)