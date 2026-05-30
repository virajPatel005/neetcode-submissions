class MyHashSet:

    def __init__(self):
          self.dicti=[]

        

    def add(self, key: int) -> None:
        if key not in self.dicti:
            self.dicti.append(key)
            return None
        else:
            return

        

    def remove(self, key: int) -> None:
        if key not in self.dicti:
            return 
        else:
            self.dicti.remove(key)
        return None 

        

    def contains(self, key: int) -> bool:
        if key in self.dicti:
            return True
        else:
            return False



        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)