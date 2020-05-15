# abs() returns the absolute value of a number
# print(abs(2 - 9))

# all() returns True if all items in an iterable object are true
# print(all([0, 2, 3])) //False
# print(all([1, 2, 3])) //True

# any() returns True if any item in an iterable object is True
# print(any([0, 1, 2, 3])) //True

# bin() returns the binary version of a number
# print(bin(3023))

# bool() returns the boolean value of the specified object
# print(bool(30)) // true

# chr() returns the character from the specified Unicode code
# chr(97) // a

# delattr() deletes the specified attribute (property or method) from the specified object
# delattr(object, attribute)

# dict() returns a dictionary (Array)
# x = dict(name = "Jen", age = 24, country = "USA")
# print(x) //{'name': 'Jen', 'age': 24, 'country': 'USA'}

# dir() returns a list of the specified object's properties and methods
# print(dir(x))

# divmod() returns the quotient and the remainder when argument1 is divided by argument2
# divmod(divident, divisor)
# x = divmod(5, 2)
# print(x) //(2, 1)

# enumerate() takes a collection (e.g. a tuple) and returns it as an enumerate object. The function adds a 
# counter as the key of the object
# enumerate(iterable, start)
# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
# print(list(y)) //[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# filter() use a filter function to exclude items in an iterable object 
# def is_even(number):
#     return number % 2 == 0
# print(list(filter(is_even, [1, 2, 3, 0]))) //[2, 0]

# float() returns a floating point number
# print(float(33)) //33.0

# format() formats a specified value 
# print(format(0.5, '%')) //50.000000%

# frozenset() returns an unchangeable frozenset object (like a set that's frozen)
# mylist = ['apple', 'banana', 'cherry']
# print(frozenset(mylist)) //frozenset({'banana', 'cherry', 'apple'})

# getattr() returns the value of specified attribute from the specified object 
class Person: 
    name = 'Jen' 
    age = 24 
    gender = 'female'
# print(getattr(Person, 'gender')) // female

# hasattr() returns True if the specified object has the specified attribute (property/method)
# print(hasattr(Person, 'hobby')) //False
# print(hasattr(Person, 'name')) //True

# hash() returns the hash value of a specified object 
# ?????

# hex() converts a number into a hexadecimal value
# print(hex(33))

# input() allows user input
# print("Enter your name:")
# x = input()
# print("Hello, " + x)

# int() returns an integer, like parseInt
# print(int('9'))

# isinstance() returns True if the specified object is of the specified type, otherwise False
# isinstance(object, type)
# print(isinstance(5, int)) //True
# print(isinstance(5, str)) //False
# print(isinstance("Hello", (float, int, str, list, dict, tuple))) //True

# issubclass() returns True if the specified object is a subclass of the specified object,
# otherwise return False
# issubclass(object, subclass)

# iter() returns an iterator object
# x = iter(["apple", "banana", "cherry"])
# print(next(x)) //apple
# print(next(x)) //banana
# print(next(x)) //cherry

# len() returns the length of an object
# print(len([1, 2])) //2





