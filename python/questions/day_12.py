"""
Question 47: 
How would you implement a simple LRU cache in Python?

from collections import OrderedDict



class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
"""

"""
46. How would you find the first non-repeated character in a string?

from collections import OrderedDict

string = "abracadabra"

def first_non_repeated_char_dict(string: str):
    count = OrderedDict()

    for char in string:
        count[char] = count.get(char, 0) + 1
    for char, freq in count.items():
        if freq == 1:
            return char
    return None

def first_non_repeated_char(string: str):
    repeated_letters = []
    non_repeated_letters = []
    for letter in string:
        if letter in repeated_letters:
            continue
        elif letter not in non_repeated_letters:
            non_repeated_letters.append(letter)
        else:
            non_repeated_letters.remove(letter)
            repeated_letters.append(letter)
    return non_repeated_letters[0]

print(first_non_repeated_char(string))
print(first_non_repeated_char_dict(string))
"""
