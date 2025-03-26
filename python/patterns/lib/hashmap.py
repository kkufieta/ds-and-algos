class HashMap:
    def __init__(self):
        keyspace = 333331
        self.table = [Bucket()]*keyspace
        self.hash_fcn = lambda key: key%keyspace

    def put(self, key, value):
        self.table[self.hash_fcn(key)].put(key, value)

    def get(self, key):
        return self.table[self.hash_fcn(key)].get(key)
    
    def remove(self, key):
        self.table[self.hash_fcn(key)].remove(key)


class Bucket:
    def __init__(self):
        self.items = []

    def put(self, key, value):
        for i, (_key, _) in enumerate(self.items):
            if _key == key:
                self.items[i] = (key, value)
                return
        self.items.append((key, value))

    def get(self, key):
        for _key, val in self.items:
            if _key == key:
                return val
        return -1

    def remove(self, key):
        for i, (_key, _) in enumerate(self.items):
            if _key == key:
                self.items.pop(i)
