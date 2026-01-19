class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        hash_value = 0
        for i in string:
            hash_value += ord(i)
        return hash_value
    
    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        else:
            self.collection[hash_value] = {key: value}

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]
        else:
            return
    
    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]
            else:
                return None
        else:
            return None