class HashTable:
    def __init__(self, size):
        self.elements = [None for i in range(size)]
        self.count = size

    def hash(self, key):
        return key % self.count

    def add(self, key, value):
        addr = self.hash(key)
        while self.elements[addr] is not None:
            addr = (addr + 1) % self.count
        self.elements[addr] = value

    def contains(self, key):
        star = addr = self.hash(key)
        while self.elements[addr] != key:
            addr = (addr + 1) % self.count
            if not self.elements[addr] or addr == star:
                return False
        return True


hash_table = HashTable(5)
hash_table.add(1, 1)
hash_table.add(2, 2)
hash_table.add(3, 3)
hash_table.add(4, 4)
hash_table.add(5, 5)
print(hash_table.contains(1))
print(hash_table.contains(2))
print(hash_table.contains(3))
print(hash_table.contains(4))
print(hash_table.contains(5))
print(hash_table.contains(6))
print(hash_table.contains(7))
print(hash_table.contains(8))
print(hash_table.contains(9))
print(hash_table.contains(10))
