# Big O Time: Insertion O(1), deletion O(1), Access O(1). Space: O(n)
# Hash tables super fast and great for storing and accessing data. How good
# a hash function is depends on hash function and how well it minimises
# collisions - use primes! This is for NON CRYPTOGRAPHIC hashes as only part
# of the data is used to make the hash key. Good hash function (for hash
# tables): Fast, distributes keys evenly in hash table, handles duplicates (
# open addressing(e.g. linear probing, random probing - cpython uses this,
# double hashing etc vs chaining - multiple data at same address e.g. in an
# array), and minimise collisions. Modern hash tables also dynamically
# resize i.e. rehash e.g. python's hash tables resize after 2/3 full. Some
# can size down to save memory as well as size up. The function MUST be
# deterministic i.e return the same hash key given a certain key so can't
# use pseudorandom generators!
# Hash Tables - store key value pairs. Can find values quickly given a key.
# They store data in a large array by hashing keys.
class HashTable:
    def __init__(self, size=10):
        self.key_map = [None] * size

    def __repr__(self):
        return f"{HashTable.__name__}"

    def _hash(self, key):
        total = 0
        WEIRD_PRIME = 31
        for i in range(min(len(key), 100)):
            char = key[i]
            value = ord(char) - 96
            total = (total * WEIRD_PRIME + value) % len(self.key_map)

        return total

    # does not handle duplicate keys - should warn user
    def set(self, key, value):
        hashed_key = self._hash(key)
        if self.key_map[hashed_key] is None:
            self.key_map[hashed_key] = [[key, value]]
        else:
            temp = [[key, value]]
            for i in self.key_map[hashed_key]:
                temp.append(i)
            self.key_map[hashed_key] = temp
        return hashed_key

    def get(self, key):
        hashed_key = self._hash(key)
        if self.key_map[hashed_key] is None:
            return None
        for i in self.key_map[hashed_key]:
            if i[0] == key:
                return i[1]
        return None

    def keys(self):
        all_keys = []
        for i in self.key_map:
            if i is None:
                pass
            elif len(i) > 1:
                for j in i:
                    all_keys.append(j[0])
            else:
                all_keys.append(i[0])
        return all_keys

    def values(self):
        all_values = []
        for i in self.key_map:
            if i is None:
                pass
            elif len(i) > 1:
                for j in i:
                    if j[1] not in all_values:
                        all_values.append(j[1])
            else:
                if i[0][1] not in all_values:
                    all_values.append(i[0][1])
        return all_values
