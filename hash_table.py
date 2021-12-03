class HashTableElement:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.length = 0
        self.table = [None] * capacity

    def set_value(self, key, value):
        self.length += 1
        index = self.get_hash(key)
        hash_element = self.table[index]
        if hash_element is None:
            self.table[index] = HashTableElement(key, [value])
        else:
            hash_element.value = [value] + hash_element.value

    def get_value(self, key):
        index = self.get_hash(key)
        hash_element = self.table[index]
        return hash_element.value[0]

    def get_hash(self, key):
        hashsum = 0
        for idx, symbol in enumerate(key):
            hashsum += (idx + len(key)) ** ord(symbol)
        hashsum %= hashsum % self.capacity
        return hashsum
