"""
SOLID PRINCIPLES

- "S" stands for Single Resposability Principle:
This principle states that each part of code, method or class should have only one
responsability. We could use an analogy here to ilustrate the theory behind it, let´s
say we have a restaurant and in this restaurant we have a cooker that is responsible for
cooking high quality food for our clients. If the cooker starts doing other tasks such
as delivering the food on the table, cleaning the floor or gathering the payments the
food quality would decrease by a lot.
On our code we should follow the same logic, having each class or method design for a
single responsability.


- "O" stands for Open/Close principle:
This principle states that a class should be closed for modification but open for exten-
sions. Let's say you have a class PaymentProcessor. Initially, the class supports credit
card payment processing, if you wanted to add a new feature into this class you would
have to change the main core class logic. Applying this principle, you could have a Base
class PaymentProcessor and new payment logic features could have their own classes
inheriting from the main class.

Ex:
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def processPayment(self):
        '''Implement the logic of the given payment type'''
        pass


class CreditCardPayment(PaymentProcessor):
    def __init__(self):
        super().__init__()
    
    def processPayment(self):
        print("Processing credit card payment")


class PayPalPayment(PaymentProcessor):
    def __init__(self):
        super().__init__()
    
    def processPayment(self):
        print("Processing paypal payment")

        
- "L" stands for Liskov's Substitution Principle:
This principle states that child classes have to have the same behavior of base classes
meaning that you can alter the base class for the child class in the code without breaking
the logic.

Follow bellow an example in which this principle is broken:

class Rectagle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def calc_area(self):
        return self.width * self.height


class Square(Rectagle):
    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.height = self.width = height
    
    def __repr__(self):
        return f"{self.width, self.height}"
    
def resize_and_print_area(rect: Rectagle):
    height = 5
    width = 10
    rect.set_height(height)
    rect.set_width(width)
    print(f"output: {rect.calc_area()}, expected output: {height*width}")

resize_and_print_area(Rectagle(2, 3))
resize_and_print_area(Square(2, 3))

- "I" stands for Interface Segregation Principle
This principle is the first principle that applies to Interfaces instead of classes in 
SOLID and it is similar to the single responsibility principle. It states that "do not 
force any client to implement an interface which is irrelevant to them". Here your main 
goal is to focus on avoiding fat interface and give preference to many small 
client-specific interfaces. You should prefer many client interfaces rather than one 
general interface and each interface should have a specific responsibility.

Let's understand Interface Segregation Principle using an example:

Suppose if you enter a restaurant and you are pure vegetarian. The waiter in that 
restaurant gave you the menu card which includes vegetarian items, non-vegetarian items, 
drinks, and sweets. 

In this case, as a customer, you should have a menu card which includes only vegetarian 
items, not everything which you don't eat in your food. Here the menu should be different 
for different types of customers.
The common or general menu card for everyone can be divided into multiple cards instead 
of just one. Using this principle helps in reducing the side effects and frequency of 
required changes.

- "D" stands for Dependendy Inversion Principle
The Dependency Inversion Principle (DIP) is a principle in object-oriented design that 
states that "High-level modules should not depend on low-level modules. Both should 
depend on abstractions". Additionally, abstractions should not depend on details. 
Details should depend on abstractions.

Ex:
from abc import ABC, abstractmethod


class IDataBase(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def create_connection(self):
        '''This method should implement database connection'''
        pass


    @abstractmethod
    def store_data(self, data):
        '''This method should implement storing new data'''
        pass


class PostgresDataBase(IDataBase):
    def __init__(self, connection_string: str):
        self.service_name = "Postgres"
        self.connection_string = connection_string
    
    def create_connection(self):
        print(f"Connection to {self.service_name} was established")

    def store_data(self, data):
        log_message = {
            "data": data,
            "message": f"Data was stored to {self.service_name}"
        }
        print(log_message)


class MySqlDataBase(IDataBase):
    def __init__(self, connection_string: str):
        self.service_name = "MySql"
        self.connection_string = connection_string
    
    def create_connection(self):
        print(f"Connection to {self.service_name} was established")

    def store_data(self, data):
        log_message = {
            "data": data,
            "message": f"Data was stored to {self.service_name}"
        }
        print(log_message)


class DataConsumer:
    '''This is class is responsible for consuming data and store into a database'''
    def __init__(self, data_base: IDataBase):
        self.data_base = data_base
    
    def insert_data_to_db(self, data):
        self.data_base.store_data(data)

data = {
    "instrument": "BTC",
    "price": 100000
}
data_consumer_1 = DataConsumer(MySqlDataBase(connection_string="test"))
data_consumer_1.insert_data_to_db(data=data)
data_consumer_2 = DataConsumer(PostgresDataBase(connection_string="test"))
data_consumer_2.insert_data_to_db(data=data)
"""

