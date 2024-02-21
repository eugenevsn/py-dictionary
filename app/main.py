class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.table = [None] * self.capacity
        self.count = 0

    def __getitem__(self, key):
        hash_key = hash(key)
        index = hash_key % self.capacity
        while self.table[index]:
            if self.table[index][0] == hash_key and \
                    self.table[index][1] == key:
                return self.table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError(f"Key: {key} not found!")

    def __setitem__(self, key, value):
        self.resize()

        hash_key = hash(key)
        index = hash_key % self.capacity
        while self.table[index]:
            if self.table[index][0] == hash_key and \
                    self.table[index][1] == key:
                self.table[index][2] = value
                self.count -= 1
                break
            else:
                index = (index + 1) % self.capacity
        self.table[index] = [hash_key, key, value]
        self.count += 1

    def __len__(self):
        return self.count

    def __repr__(self):
        return str({key[0]: key[-1] for key in self.table if key is not None})

    def resize(self):
        if self.count > self.capacity * 2 / 3:
            self.capacity *= 2

            copy_table = self.table.copy()
            self.table = [None] * self.capacity
            self.count = 0
            for element in copy_table:
                if element:
                    self.__setitem__(element[1], element[2])
