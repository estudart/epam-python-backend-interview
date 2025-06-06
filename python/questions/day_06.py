import time

"""
Question 38:
How would you sort a list of dictionaries by a specific key?

test_list = [
    {"name": "erico"},
    {"name": "antonio"}
]
key="name"

def sort_list_by_dict_key(test_list: list[dict], key):
    test_list.sort(key=lambda x: x[key])
    return test_list

print(sort_list_by_dict_key(test_list, key))
"""


"""
Question 40:
How would you implement a retry mechanism for a function that might fail?

def retry_decorator(max_retries, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if attempt == max_retries:
                        raise err
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_decorator(max_retries=3, delay=1)
def fail_function():
    return 3/0

print(fail_function())
"""


"""
Question 41:
How would you implement a simple rate limiter for a function in Python?

# The hint here is to store the state on list[0]

def rate_limiter(calls_per_second):
    interval = 1/calls_per_second
    last_call_time = [0]
    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed_time = time.time() - last_call_time[0]

            if elapsed_time < interval:
                print("Rate limite exceeded")
                time.sleep(elapsed_time)

            last_call_time[0] = time.time()
            return func(*args, **kwargs)                  
        return wrapper
    return decorator
"""


"""
Question 42:
How would you flatten a nested list in Python?

test_list = [
    1,
    [1,2,[1,2]],
    [1, 2, 3]
]

def flatten_list(test_list: list[list]):
    flattened_list = []
    for item in test_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list
print(flatten_list(test_list))
"""
