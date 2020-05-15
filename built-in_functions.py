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

# list() returns a list object. A list object is a collection which is ordered and changeable.
# print(list((1, 2, 3))) // [1, 2, 3]

# map() returns the specified iterator with the specified function applied to each item
# map(function, iterables)
# print(list(map(lambda x: x + 5, [1, 2, 3]))) // [6, 7, 8]

# max() returns the largest item in an iterable 
# print(max(1, 2, 3, 0, -2)) //3
# print(max('a', 'b', 'x')) // x
# print(max([1,2,3,6,5,4])) // 6

# min() returns the smallest item in an iterable
# print(min(1,4,52,4,-4,10)) //-4

# arr = iter([1,4,3,8,4,2,6])
# print(next(arr)) //1
# print(next(arr)) //4
# print(next(arr)) //3
# print(next(arr)) //8

# object() returns a new object 

# oct() converts a number into an octal
# print(oct(93)) //0o135

# ord() convert an integer representing the Unicode of the specified character 
# print(ord('a')) //97
# j = ord('j')
# print(chr(j)) //j

# pow() returns the value of x to the power of y 
# print(pow(2,3)) //8
# print(pow(3,3)) //27

# range() returns a sequence of numbers, starting from 0 and incrementing by 1 (by default)
# print(list(range(8))) // [0, 1, 2, 3, 4, 5, 6, 7]

# reversed() returns a reversed iterator
# x = [1, 2, 3, 4, 5]
# print(list(reversed(x))) // [5, 4, 3, 2, 1]

# round() rounds a number to the nearest integer
# print(round(3.55)) //4
# print(round(3.2)) //3

# set() returns a new set object (unordered, with unique values)
# x = set((1, 2, 3))
# y = set(('a', 'p', 'p', 'l', 'e'))
# print(x) //{1, 2, 3}
# print(y) //{'a', 'p', 'l', 'e'}

# setattr() sets an attribute (property/method) of an object
# setattr(object, attribute, value)

# setattr(Person, 'age', 40)
# print(getattr(Person, 'age')) //40
# setattr(Person, 'height', 61)
# print(getattr(Person, 'height')) //61

# slice() returns a slice object 
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(2)
# print(a[x]) //('a', 'b')
# print(a[slice(4)]) //("a", "b", "c", "d")
# print(a[slice(1,4)]) //("b", "c", "d")

# sorted() returns a sorted list of the specified iterable object 
# sorted(iterable, key=key, reverse=reverse)
# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x) //['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# nums = [1, 2, 3, 4, -2, 3, 0]
# print(sorted(nums)) //[-2, 0, 1, 2, 3, 3, 4]
# print(sorted(nums, reverse=True)) //[4, 3, 3, 2, 1, 0, -2]
# print(sorted(a, reverse=True)) //['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

# str() returns a string object 
# print(str(399)) 

# sum() sums the items of an iterator
# print(sum((1,2,3,4))) //10
# arr = [10, 3, 95, 30]
# print(sum(arr)) //138

# super() returns an object that represents the parent class. It is used to give access to 
# methods and properties of a parent or sibling class.

# tuple() creates a tuple object. Note that you cannot change or remove items in a tuple
# print(tuple([1,5,7,3])) //(1, 5, 7, 3)
# print(tuple('jen')) //('j', 'e', 'n')

# type() returns the type of an object
# print(type(19)) //class 'int'

# zip() returns a zip object, which is an iterator of tuples where the first item in
# each passed iterator is paired together, then the second item in each passed iterator are paired together, etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator
# x = (1, 2, 3)
# y = ('a', 'b', 'c')
# a = (1, 2, 3, 4)
# b = (4, 5, 6)
# print(list(zip(a,b))) //[(1, 4), (2, 5), (3, 6)] last element in a is cut off
# print(list(zip(x,y))) //[(1, 'a'), (2, 'b'), (3, 'c')]


