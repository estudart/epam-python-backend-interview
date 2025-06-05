"""
Question 22:
What is the purpose of the `__call__` method in Python?

'__call__' is a special method in Python that allows classes to be called as functions
allowing objects to encapsulate logic and state, offering a more flexible and expressive
way to write code.

class Adder:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, x):
        return self.value + x
    
add_five = Adder(5)
test_1 = add_five(10)
test_2 = add_five(20)
print(test_1, test_2)
"""

"""
Question 23:
What is the purpose of the `__slots__` attribute in Python?
"""

"""
Question 24:
What is the difference between `iter()` and `next()` functions in Python?

The difference between iter() and next() is that iter() receives an iterable object
such as lists and tuples, and returns an iterator object containing the elements of the
iterable. next() in the other hand, gets the iterator object and returns the next
element after last one returned.

my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# Attempting to get the next element raises StopIteration
try:
    print(next(my_iterator))
except StopIteration:
    print("End of iteration")
"""

"""
Question 31:
What is the purpose of the `threading` and `multiprocessing` modules in Python?

threading is a module design to work with threads in python, threads are async io
tasks that run on name core of python. And because of GIL, those threads are not
parallel.
multiprocessing is a module design to work with Process, those processes run on
different cores of the machine and do not share memory, yet they are fully parallel.
"""


"""
Question 34:
How would you merge two dictionaries in Python?

dict_1 = {
    "a": 1, 
    "b": 2
}

dict_2 = {
    "b": 3,
    "c": 4
}

merge_dict = {
    **dict_1,
    **dict_2
}
print(merge_dict)
"""

"""
Question 35: 
How would you remove duplicate elements from a list while preserving the order?

test_list = [1, 1, 4, 3, 5, 6, 7]

def unique_list(test_list: list) -> list:
    seen = set()
    unique_list = []

    for n in test_list:
        if n not in seen:
            seen.add(n)
            unique_list.append(n)
            
    print(unique_list)
    return unique_list

unique_list(test_list=test_list)
"""

"""
Question 37:
How would you find the intersection of two lists in Python?

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

def find_intersection(list_1: list, list_2: list) -> list:
    list_2_set = set(list_2)
    intersection_list = [
        item for item in list_1
        if item in list_2_set
    ]
    print(intersection_list)
    return intersection_list

find_intersection(list_1, list_2)
"""