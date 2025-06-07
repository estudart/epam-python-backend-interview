"""
Q1: What is the difference between is and == in Python? Provide an 
example where the result differs.

is statement is used to check if both values are inside the same
place in the memory. In the other hand, '==' is used to check is two
values are the same.

Ex:
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

person_1 = Person('Erico')
person_2 = Person('Erico')

def is_the_same_person(person_1, person_2):
    return person_1 is person_2

def is_name_equal(person_1: Person, person_2: Person):
    return person_1.name == person_2.name

print(f"Are they the same person? {is_the_same_person(person_1, person_2)}")
print(f"Do they have the same name? {is_name_equal(person_1, person_2)}")

##############################################################################

Q2: What is a Python generator, and how is it different from a list 
comprehension?

List comprehension: [x for x in range(10)] → returns a full list in memory.

Generator: (x for x in range(10)) → returns a generator object, which yields 
one item at a time (lazy evaluation).

##############################################################################

Q3: What will this code print and why?

def append_to(element, target=[]):
    target.append(element)
    return target

print(append_to(1))
print(append_to(2))

Python uses the same list object for target across function calls because 
default arguments are evaluated only once at function definition time.

def append_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

##############################################################################

Q4: Explain the concept of method resolution order (MRO) in multiple inheritance.

The concept of MRO is related to how python handles multiple inheritence. If a class
inherits from two parents, the MRO can come in action. For example if I have a class
Developer that devides from Person, Python knows to call the function inside Developer
class because of MRO.

Ex:
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def talk(self):
        print(f"Hello, I'm Érico")

class Developer(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def talk(self):
        print(f"Hello, I love Python")

epam_developer = Developer('Érico')
epam_developer.talk()

##############################################################################

Q5: What are @staticmethod, @classmethod, and instance methods? When should each be used?

staticmethods: Those are methods that belongs to the class itself but not an specific instance.
They can be used with the @staticmethod decorator, passing its parameters. Remember not to use
self as a parameter in this case.

instance methods: Those are methods that are inside a given instance of the class. Here we dont
need to use any decorator, just explicity define it inside the class methods and remember to pass
self as parameter.

classmethod: uses cls as first argument and is often used for alternative constructors.

##############################################################################

Q6: Design a base class User and two subclasses AdminUser and RegularUser with different behavior 
for a method get_permissions().

class User:
    def __init__(self, permissions):
        self.permissions = permissions

    def get_permissions(self) -> dict:
        pass

class AdminUser(User):
    def __init__(self, permissions):
        super().__init__(permissions)
    
    def get_permissions(self) -> dict:
        message = {
            "status": True,
            "message": self.permissions
        }
        return message

class RegularUser(User):
    def __init__(self, permissions):
        super().__init__(permissions)
    
    def get_permissions(self) -> dict:
        message = {
            "status": False,
            "message": "Access denied"
        }
        return message

regular_user = RegularUser("9879879654654")
admin_user = AdminUser("admin@password")

print(regular_user.get_permissions())
print(admin_user.get_permissions())

##############################################################################

Q7: Explain the difference between deepcopy and copy in Python with a nested list example.

The main difference between a copy and a deepcopy is related to how those two copies are
handled on the computers memory. While a copy (shallow copy) will refer to the same space
in memory, a deepcopy will actually create a new object in the memory completely decoupled
from the original object.

import copy

original_list = [1, [2, 3, 4], 6, 7]

shallow_copy = original_list.copy()
shallow_copy[1].append(5)
print(f"Shallow copy: {shallow_copy}")
print(f"Original copy: {original_list}")

deep_copy = copy.deepcopy(original_list)
deep_copy[1].append(10)
print(f"Deep copy: {deep_copy}")
print(f"Original copy: {original_list}")


##############################################################################

Q8: What is the purpose of collections.defaultdict? How is it different from dict.get()?

defaultdict automatically creates default values for missing keys.

Ex:
from collections import defaultdict

d = defaultdict(int)  # default value = 0
d['a'] += 1

While dict.get() method will just retrieve a given value from a dict by searching the
provided key
##############################################################################

Q9: What does this code do?

import itertools
print(list(itertools.permutations('AB', 2)))

Dont know the answer

##############################################################################

Q10: How would you find the most frequent word in a large text file using the standard library?

from collections import Counter

with open('file.txt') as f:
    words = f.read().split()
    most_common = Counter(words).most_common(1)
print(most_common)


##############################################################################

Q11: What tools do you use to profile memory usage in Python? Mention at least two.

Dont know the answer

##############################################################################

Q12: What is the time complexity of searching in a list vs a set?

list -> O(n)
dict -> O(1)

##############################################################################

Q13: What is the difference between threads and async coroutines in Python?

The main difference between async and threads is that threads lock the main execution
process when they are running, whenever my threads is running the main app stops
for a short while. Async has a different approach, it unlocks the main process and
retrieve the result whenever the coroutine is done.

##############################################################################

Q14: Write a minimal async function that downloads three URLs concurrently using aiohttp.

import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    urls = ['https://example.com'] * 3
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch(session, url) for url in urls))
    print(results)

asyncio.run(main())

##############################################################################

Q15: What is the difference between pip freeze and pip list?

pip freeze comand is used to generate a file having all the requirements that are being used in
the current python environment. pip list in the other hand can be used to list all 
depencies that are been used in the current application environment

##############################################################################

Q16: What is a pyproject.toml file? When and why would you use it?

Dont know the answer

##############################################################################

Q17: Explain the difference between unit tests and integration tests. When should you mock something?

Units tests are designed to test a service on its own. Let's say we have an API app running
a unit test would be design to test all routes and see wether they return errors or wrong answers.
An integration test would have a different approach meaning that the goal here is to understand how
the communication and integration between different services or microservices and going.

Unit test: test individual functions or methods in isolation.

Integration test: test interaction between components, like DB, APIs, etc.

✔ Mocking is for unit tests when you want to isolate external dependencies.

##############################################################################

Q18: Write a simple test for the function add(a, b) using pytest.

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

##############################################################################

Q19: How would you design a simple rate limiter using Python?

import time

def rate_limiter(calls_per_second):
    interval = 1/calls_per_second
    last_call = [0]
    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed_time = time.time() - last_call[0]
            
            if elapsed_time < interval:
                time.sleep(interval - elapsed_time)

            last_call[0] = time.time()
            return func(*args, **kwargs)

        return wrapper
    return decorator

##############################################################################

Q20: What’s the difference between @lru_cache and manually storing results in a global dict?

A lru_chache has slightly some different features. First of all it has a fixed number of results
this helps on managing memory, because if an item gets too old it will be removed from cache.
The order of this cache will always be based on the lated used value, meaning that this one
will go to the top of this object
"""

"""
---

## 🧠 Python Topics to Study More

Based on your answers, here are **recommended topics to review or dive deeper into**:

### ✅ Solid Understanding (Good job!)

* `is` vs `==`
* Shallow vs deep copy
* Python decorators (e.g. `@staticmethod`)
* Inheritance and MRO
* Basic class design
* `pip freeze` vs `pip list`
* Difference between threads and `async`
* Writing a basic `rate_limiter`
* Complexity of search in list vs set

### 📘 Recommended Topics to Study More

#### 🔁 Generators vs List Comprehensions

* Yield keyword
* Memory efficiency
* Use cases for streaming data

#### 🧠 Mutable Default Arguments

* Why `append_to(2)` returns `[1, 2]` (the same list is reused!)
* Fix with `target=None` pattern

#### 📦 `collections.defaultdict`

* Automatically initialize default values
* Use cases like counting, grouping

#### 🧮 `itertools.permutations`

* Combinatorics: permutations, combinations
* Iterable utilities from `itertools`

#### 🧑‍🏫 `unittest` vs `pytest`

* How to write assertions
* `pytest` fixtures and parametrization

#### 🧪 Unit vs Integration Testing

* How to use `unittest.mock` or `pytest-mock`

#### 🔍 Profiling Tools

* `memory_profiler`
* `tracemalloc`
* `cProfile`, `line_profiler`

#### 📂 `pyproject.toml`

* Modern Python packaging (PEP 518)
* How it replaces `setup.py` in many projects

#### 📄 Most Frequent Word in File

* File I/O
* Using `collections.Counter`
* `.split()` and basic cleaning

#### 🧱 `@lru_cache` vs manual caching

* From `functools`
* Automatic memory management (LRU eviction)
* Good for memoization

---
"""