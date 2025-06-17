"""
Given a list of integers, find the pair with the smallest absolute difference.

test_list = [1, 4, 7, 2, 8, 10]


def find_smallest_dif(test_list):
    sorted_list = sorted(test_list)
    min_dif = float('inf')
    pair = []

    for i in range(len(sorted_list)-1):
        dif = abs(sorted_list[i] - sorted_list[i+1])
        
        if dif < min_dif:
            min_dif = dif
            pair = [sorted_list[i], sorted_list[i+1]]

    return pair
      

print(find_smallest_dif(test_list))
"""

"""

## ✅ Python Backend Mock Interview (Verbal, Reasoning + Some Light Coding)

---

### 🎯 Section 1: Python Theory / OOP / Internals (No coding, just explain)

1. **What is the difference between a `classmethod`, `staticmethod`, and an instance method 
in Python?**

staticmethods ate methods that belong to all classes, with this said, they do not rely on any
class attributes. You can use them by decorating the method with @staticmethod in Python

instancemethod is a method that belongs to the specific instance that you are calling it from
oftenly it relys on the classes atributes and should be implemented by using "self" as a para
meter of the method.

2. **Explain Python's GIL (Global Interpreter Lock). When does it matter?**


3. **What’s the difference between shallow copy and deep copy in Python?**

The difference between shallow copy and deep copy is basically on how it is managed on the me
mory. 
Shallow copies are stored in the same place of the memory, and it is "shallow" because
if you make changes on nested items within the object, those changes will be reflected in the
copy.
On the other hand, a deep copy goes one step forward and generate a copy of the object in a 
different place of the memory. So both objects a completed decoupled, if you update a nested
item within the object, this change wont reflect in the other.

Ex:
import copy

test_list = [1, 2, 3, [4, 5], 6]
shallow_copy = test_list.copy()
deep_copy = copy.deepcopy(test_list)

test_list[3][0] = 10
print(test_list)
print(shallow_copy)
print(deep_copy)

4. **Explain how list comprehensions work in Python and give an example.**

List comprehension are a dinamic way of iterating through objects and create a list out of
it. We can have a iteration on a dictionary, operate a function on it and later on create
a list out of it in just on line.

Ex:
mapping_dict_test = {
    "Empire State": 2000,
    "Burj Khalifa": 3000
}

hights_list = []

for name, hight in mapping_dict_test.items():
    hights_list.append(hight)

print(hights_list)

hights_list = [hight for name, hight in mapping_dict_test.items()]
print(hights_list)

5. **What’s the difference between mutable and immutable objects in Python? Give examples.**

Mutable objects are objects in which you can updated items within the object, an example of
so would be dictionaries and list in python.
In the other hand immutable objects are those that cant be changed once you insert a value on
it, in python a good example of immutable objects are lists

6. **How does Python manage memory for objects?**

7. **Explain what a decorator is and give a practical use case for it.**
A decorator is a method that can be called as default before or after a function is called in
python. A practical use case for it would be to implement a decorator with retry logic.

import time

def retry_decorator(max_retries, delay_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f"Could not run function, reason: {err}")
                time.sleep(delay_time)
        return wrapper
    return decorator

8. **What is dependency injection and how would you implement a simple example of it in Python?**

Depency injection is a techinique used in software development in which classes should not depend on
another especif class on your application, having this in mind, your code can be fully decoupled. If
for some reason the class needs another dependency in the future, you need to do minor updates in the code
A good example of it could be connection with databases, in this scenario is possible to create an interface
responsbile for hadling database connection especifying the methods needed to implement. Then, in the
future is super simple to migrate your code from one especific database to another.

---

### 🎯 Section 2: REST / API Design

9. **If you were building a REST API for a book store, what would be your typical REST 
endpoints (CRUD)?**

POST /book, /book-store
GET /book, /book-store

10. **What’s the difference between PUT and PATCH in REST APIs?**

PUT update the entire object while PATCH updates only specific attributes of a given object.

11. **How would you handle validation and error responses in a FastAPI or Flask API?**

12. **How do you implement pagination in a REST API?**

---

### 🎯 Section 3: Problem Solving / Light Coding (Verbal or quick-code)

*(You don’t need to code full functions, just explain your logic or write small snippets)*

13. **Given a list of integers, find the most frequent element.**

(→ Expected thinking: Use `collections.Counter` or dict to count frequencies)

list_to_count = [1, 2, 4, 3, 3, 3, 6, 7, 7]

def list_freq(list_to_count):
    freq_dict = {}

    for num in list_to_count:
        if not freq_dict.get(num):
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
    
    print(max(freq_dict.values()))

list_freq(list_to_count)

---

14. **Given this input list: `[1,2,2,3,4,4,5]`, return a new list with only unique elements 
(no duplicates, order preserved).**

(→ Expected thinking: Use `set` with an iteration, or OrderedDict, or manual filtering)

---

15. **Given a nested dictionary (like a JSON), write logic to flatten it.**

Example:

```python
input = {'a': 1, 'b': {'c': 2, 'd': 3}}
output = {'a': 1, 'b.c': 2, 'b.d': 3}
```

(→ Expected: Recursion or stack-based flattening)

---

### 🎯 Section 4: SQL (Verbal)

16. **How would you write a SQL query to find the second highest salary from an employee 
table?**

(→ Either use `LIMIT OFFSET`, or `MAX WHERE salary < (SELECT MAX(salary))`)

---

17. **What is a JOIN? Explain the difference between INNER JOIN and LEFT JOIN with 
an example.**

18. **What’s the difference between WHERE and HAVING in SQL?**

---

### 🎯 Section 5: Troubleshooting / Debugging Scenarios (Verbal Reasoning)

19. **You deployed a new REST API endpoint, and users are reporting 500 errors. Walk me 
through your debugging steps.**

20. **A production API suddenly started responding very slowly. What are your first diagnostic 
steps?**

---

---

If you want, I can pick a few from here and simulate being the EPAM interviewer and you answer as if in the interview.
Or… I can help you write answers for each one (to rehearse).

👉 **Which do you prefer?**

* Verbal mock (you answer live)?
* Help drafting written answers for all?
* Or I pick random 5-7 and quiz you?

"""


