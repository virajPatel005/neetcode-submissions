class MyHashMap:

    def __init__(self):
        self.li=[[] for i in range(100)]

        
        

    def put(self, key: int, value: int) -> None:
        bucket=key%len(self.li)
        for i in self.li[bucket]:
            if i[0]==key:
                i[1]=value
                return None
            
        self.li[bucket].append([key,value])
        return None


        

    def get(self, key: int) -> int:
        bucket=key%len(self.li)
        for i in self.li[bucket]:
            if i[0]==key:
                return i[1]
            
        return -1
        

    def remove(self, key: int) -> None:
        bucket=key%len(self.li)
        for i in self.li[bucket]:
            if i[0]==key:
                self.li[bucket].remove(i)
                return None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)