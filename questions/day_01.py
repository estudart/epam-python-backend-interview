"""
Question 1:
What are the key features of Python?

1. Easy to learn
2. Easy syntax
3. Dinamically typed
4. Object oriented (OOP)
5. Extensive library
6. Strong community support
"""

"""
Question 2:
What are the differences between Python 2 and Python 3?


"""

"""
Question 3:
What are python data types?

Python has several built-in data types, such as:

Numerics: int, float, complex
Text: string 
Dictionaries: Those are structures that are used to map data.
Lists: This is an ordered structure in which multiple typed objects can be stored => multable
Tuples: This is another ordered structured but this time, the data is unmutable within the tuple.
Boolean: A binary represented data type, eg. True or False
"""

"""
Question 4:
How to create a function in Python?
def sum_number(a, b):
    return a + b
"""

"""
Question 5:
What is the difference between a tuple and a list in python?

Tuples are imutable and have a fixed number of "slots", which means that once you store a value on it
you can change it later on. In the other hand list a mutable objects without a fixed number of slots.
Also lists are defined with square brackets [] and tuples with parentheses ()
"""

"""
Question 6:
What are list comprehensions in Python?

List comprehensions are a concise way of generating lists in Python. For instance you can run a loop
on a data structure and at the same time create the list object. To do it you need to code the for 
loop within the square brackets. Follow bellow an exameple of how to do it on practise.

test_dict = {
    "student_1": "Erico",
    "student_2": "John"
}
test_list = [v for k,v in test_dict.items()]
print(test_list)
"""

"""
Question 7:
What is the difference between '==' and 'is' in Python?

'==' is a way to check equality between two values, and 'is' is a way of checking if the two values are
the same in memory. If we have a class of students and two students have the same first name, we could
check equality of student_1.first_name == student_2.first_name and True would be returned. In the other hand if we have the same
check with 'is' this would return False. 
"""

"""
Question 8:
Whats is a lambda function in Python?

It is a function that can be written in line such as the example bellow:
add = lambda x, y: x + y
print(add(5, 4))
"""

"""
Question 9:
How do you handle exceptions in Python?

In Python you handle exceptions by using the try/except block. Whenever a exception is found in the piece of code
an Exception will be raised and the code will jump directly to the part in which this exception is handled.
Ex:
def get_second_value_of_list(test_list: list) -> None:
    try:
        second_value_of_list = test_list[1]
    except IndexError:
        print("Second item of list was not found")
    except TypeError:
        print(f"Wrong object type: {type(test_list)}")
    else:
        print(second_value_of_list)
    finally:
        print("Search is finished")

get_second_value_of_list([0, 1])
"""

"""
Question 10:
What are function decoratoes in Python?

Decorators are functions the can run before or after another function by default.
def test_decorator(func):
    def wrapper():
        print("Function has just started")
        func()
        print("Function has just finished")
    return wrapper

@test_decorator
def say_hello():
    print("Hello!")

say_hello()
"""

"""
Question 11:
What is the global interpreter lock (GIL) in Python?
"""

"""
Question 12:
What are context managers and the `with` statement in Python?
"""

"""
Question 13:
What are metaclasses in Python?
"""

"""
Question 14:
What is the difference between '*args' and '**kwargs' in Python?

args and kwargs are ways of passing arguments into the function without defining it 
inside the function in first place.
The main difference between them is that when you use args you pass a variable as non-keyword
arguments and when you use kwargs you have to pass the arguments as keyword structure.

You can see the example bellow:
def buy_fruits(*args):
    for fruit in args:
        print(f"Buying {fruit} now :)")

buy_fruits("coconut", "apple")

def buy_fruits(**kwargs):
    fruits = kwargs.get("fruits")
    for fruit in fruits:
        print(f"Buying {fruit} now")

buy_fruits(fruits=["apple", "coconut", "banana"])
"""

"""
Question 15: 
How can you use unpacking/starred expressions (*) to assign multiple values to a variable and pass them as separate arguments to a function?
"""

"""
Question 16:
What is the difference between shallow and deep copying in Python?
Shallow copying creates a new object and inserts references to the original elements. Deep copying creates 
a new object and recursively inserts copies of the original elements. The `copy` module provides the `copy()` 
function for shallow copying and the `deepcopy()` function for deep copying.
"""

"""
Question 17:
What are Python's generators and the `yield` keyword?
"""

"""
Question 18:
What is the difference between `__str__` and `__repr__` in Python?

The difference between both of them are the use cases they apply on. For this, '__str__' would be used for client side
and '__repr__' would be used for developers to understand the definition of the object they are working with. If '__str__'
is not defined, the system will use '__repr__' as a fallback.
"""

"""
Question 19:
What are Python's descriptors?
"""

"""
Question 20:
What is the difference between `staticmethod`, `classmethod`, and instance methods in Python?

staticmethod: Static method is a mthod that belongs to class but not for an specific instance of this class. It does not have
access to the class or instance variables. You can use this on your classes by using the decorator @staticmethod.

classmethod: A class method is a method that belongs to a class and has access to class variables. It takes a reference 
to the class as its first argument and is defined using the `@classmethod` decorator.

class Animal(ABC):
    classes_dict = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Animal.classes_dict[cls.__name__] = cls

    @abstractmethod
    def speak(self):
        raise NotImplementedError

    @classmethod
    def create(cls, animal_type, **kwargs):
        if animal_type not in cls.classes_dict:
            raise ValueError(f"Unknown animal type: {animal_type}")
        return cls.classes_dict[animal_type](**kwargs)


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"

# Example usage
pet = Animal.create("Dog")
print(pet.speak())  # Woof

pet = Animal.create("Cat")
print(pet.speak())  # Meow

"""

"""
Question 21:
What is the difference between '__new__' and '__init__' in Python?

'__new__' and '__init__' are special methods in Python, the new method is called
whenever a new intance of the class is created and the init method is called whenever
this same class is initialized.
"""

"""
Question 22:
What is the purpose of the `__call__` method in Python?
"""

"""
Question 23:

"""