# create chained hash table

class HashTable:
    def __init__(self):
        self.size = 40
        self.table = [[] for i in range(self.size)]

    def _get_hash(self, key):
        hash = 0
        for char in key:
            hash += 37 ^ (ord(char))
        return hash % self.size

    def add(self, key, value):
        indexy = self._get_hash(key)
        found = False
        for indexx, data in enumerate(self.table[indexy]):
            if len(data) == 2 and data[0] == key:
                self.table[indexy][indexx] = (key, value)
                found = True
                break
        if not found:
            self.table[indexy].append((key, value))

    def get(self, key):
        index = self._get_hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def delete(self, key):
        indexy = self._get_hash(key)
        for indexx, data in enumerate(self.table[indexy]):
            if data[0] == key:
                del self.table[indexy][indexx]

    def print(self):
        print('--Packages--')
        for item in self.table:
            if item is not None:
                print(str(item))

