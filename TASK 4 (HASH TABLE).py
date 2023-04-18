# ECIE 3101 Section 1 Semester 2 Session 22/23
# Group Name: Group-Hensem-lab
# Group member:
# ABDULLAH FARHAN BIN ABD NASIR (2013219)
# MUHAMMAD NABIL ARRASYID (2011093)
# IMAN IRMANISYA BIN BAKRI (1715123)
# Ahmad Zal Hasmi Bin Ahmad Jafry (2012991)
# Muhammad Adzim Bin Rosly (2013413)
#
# TASK 4a & 4b (HASH TABLES)

class HashTable:
    # INIITIAL THE HASHTABLE
    def __init__(self,size):
        self.size = size            # initialize the size of hash tables
        self.keys = [None] * size
        self.values = [None] * size


    def __setitem__(self, key, value):
        # Checking if the Key inputted is a string key or a numerical key
        if type(key) != str:
            print("The Key of", key, "is not a string or character")
            return
        else:
            index = self.hash_func(key)

            # IF THE INDEX POSITION HAS NO KEY OR THE SAME KEY REQUESTED
            if self.keys[index] is None or self.keys[index] is key:
                self.keys[index] = key
                self.values[index] = value
                #print("New Element Added!   Updated Hash Table!")
                return
            else:
                # GOING THROUGH THE TABLE TO FIND THE EMPTY SPOT OR THE KEY
                oghash = index
                index = self.rehash_func(index)
                while index is not oghash:
                    if self.keys[index] is None or self.keys[index] is key:
                        self.keys[index] = key
                        self.values[index] = value
                        #print("New Element Added!   Updated Hash Table!")
                        return
                    else:
                        index = self.rehash_func(index)
                # IF THE TABLE IS ALREADY FULL
                print("Could not add any more element in the Hash Table")
                print("The hash table is already full")


    def __getitem__(self,key):
        index = self.hash_func(key)

        # IF THE KEY IS FOUND IMMEDIATELY
        if self.keys[index] == key:
            return self.values[index]
        else:
            # GOING THROUGH THE TABLE TO FIND THE KEY
            oghash = index
            index = self.rehash_func(index)
            while index is not oghash:
                if self.keys[index] == key:
                    return self.values[index]
                else:
                    index = self.rehash_func(index)

            print("Could not find the element in the Hash Table")
            print("The key of [", key, "] is not in the Table")


    def delete(self, key):
        # Set the index as the hashed value of the desired key
        index = self.hash_func(key)

        # If the key is initially found at the first hashed index value, delete the content of self.values
        if self.keys[index] == key:
            print("The element of '", self.values[index], "' at key '", self.keys[index], "' will be deleted")
            self.values[index] = None
            return
        else:          # If it was not found initially, rehash the index to search for the next key index
            oghash = index
            index = self.rehash_func(index)
            while index is not oghash:
                if self.keys[index] == key:
                    print("The element of '", self.values[index], "' at key '", self.keys[index], "' will be deleted")
                    self.values[index] = None
                    self.keys[index] = None
                    return
                else:
                    index = self.rehash_func(index)

            print("Could not find the element in the Hash Table")


    # HASHING FUNCTIONS
    def hash_func(self, string_key):
        hashed_key = [ord(c) for c in string_key]
        #print(hashed_key)
        return hashed_key[0] % self.size

    def rehash_func(self, hashed_index):
        return (hashed_index + 1) % self.size


print("HASH TABLE\n")
size = 5

Hash = HashTable(size)
Hash['name'] = 'Zikri'
Hash['age'] = 20
Hash['gender'] = 'M'

print(Hash['name'])
print(Hash['age'])
print(Hash['gender'])
print(Hash.keys)
print(Hash.values)

Hash['birthdate'] = '4/12/2003'
print(Hash.keys)
print(Hash.values)
print(Hash['birthdate'])

Hash['name'] = 'Hakim'
print(Hash['name'])

Hash.delete('age')
print(Hash.keys)
print(Hash.values)
print(Hash['age'])
print(Hash['birthdate'])
