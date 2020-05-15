# print('uppercase test'.upper())
# print('LOWERCASE THIS'.lower())
# print("Lowercase".endswith('e'))
# print('Lowercase'.replace('e', '@'))
# # help(str)
# print('jen is learning python'.capitalize())
# print('jen is learning python'.title())

# print(type("10.34"))

# print("art.vandelay@vandelay.co".endswith('.com'))

# van = 'vandelay.com'
# web = 'www.'
# print(web + van)

##slices first 3 characters of string
# print("7286663334"[:3])

# nothing = None


###LISTS
# travel_cities = ['Solta', 'Greenville', 'Buenos Aires', 'Los Cabos', 'Walla Walla Valley', 'Marakesh', 'Albuquerque', 'Archipelago Sea', 'Iguazu Falls', 'Salina Island', 'Toronto', 'Pyeongchang']
##accesses first element in the list
# print(travel_cities[0])
##accesses last element in the list
# print(travel_cities[-1])

##prints list items starting at first index and not including second index (at which we stop our selection of elements)
##known as slicing, but list remains intact
# print(travel_cities[0:4])

##equivalent of JS push
# travel_cities.append('New York')
# print(travel_cities[-1])
# travel_cities.pop()
# print(travel_cities[-1])

# print(travel_cities[1])
# travel_cities[1] = "Barcelona"
# print(travel_cities[1])

## The set function initializes a new set in Python.  A set is a different type collection in Python.  
## A set is just like a list, except elements do not have order and each element appears just once.
# unique_travel_cities = set(travel_cities)

##convert into a list
# unique_travel_cities_list = list(unique_travel_cities)

##find length of list
# len(unique_travel_cities_list)

###Dictionaries

# friends = {'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons': 10}
# print(friends['no_of_seasons']) #10

# ##adding a key
# friends['no_of_episodes'] = 236
# friends['best_episode'] = 'The One With The Cake'

# ##delete a key value pair
# del friends['best_episode']
# print(friends)

# friends['creators'] = ['David Crane', 'Marta Kauffman']

###LOOPS
# zero_to_three = [0, 1, 2, 3, 4]

# for number in zero_to_three:
#     print(number)

# countries = ['Croatia', 'USA', 'Argentina', 'France', 'Brazil', 'Japan', 'Vietnam', 'Israel']
# cities = ['Zagreb', 'District of Columbia', 'Buenos Aires', 'Paris', 'Rio de Janeiro', 'Tokyo', 'Hanoi', 'Tel Aviv']

# for index in list(range(0, len(countries))):
#     print(cities[index]+",", countries[index])

# example_dictionary = {'first_name': "Terrance", 'last_name': "KOAR", 'favorite_language': "Python"}
# for key, value in example_dictionary.items():
#     print("this is the key:", key)    
#     print("this is the value:", value, "\n")

# first_name = ""
# last_name = ""
# for key, value in example_dictionary.items():
#     if key == "last_name":
#         last_name = value.title()
#     if key == "first_name":
#         first_name = value
# print(first_name, last_name)

### Functions
# new_employees = ['steven', 'jan', 'meryl']
# def greet_employees():
#     welcome_messages = []
#     for new_employee in new_employees:
#         welcome_messages.append("Hi " + new_employee.title() + ", I'm so glad to be working with you!" )

#     return welcome_messages

# print(greet_employees())


### Conditionals
# def vacation_length(number_of_days):
#     if number_of_days > 4:
#         return 'that is a long vacation'
#     else:
#         return 'not so long'

# print(vacation_length(1))

# print(bool(0)) 
# print(bool(7))

# def open_restaurants(restaurants):
#     open = []
#     for restaurant in restaurants:
#         if restaurant['is_closed'] == False:
#             open.append(restaurant)       
#     return open


# The general syntax of a filter() function is given as:
# filter ( function, iterable )
# def is_even(number):
#     return number % 2 == 0

# numbers = list(range(0, 11))
# print(list(filter(is_even, numbers)))

# #A map() function is defined in python like this:
# # map(Function, Sequence)
# #The first argument is the altering function, which operates on each element 
# #by passing through the element as an argument and returning a value. 
# #The second argument is the list of elements to be iterated through and operated on. 
# #The return values of the altering function are appended to a new list, which is returned 
# #after we coerce our map object into a list.

# list(map(add_simpson, names))

# lambda can be used to define a custom function
numbers = [1, 3, 8, 9, 11, 20]
print(list(map(lambda x: x + 5, numbers)))

names = list(map(lambda restaurant: restaurant['name'], restaurants))

def cheapest_restaurants(restaurants):
    return list(filter(lambda restaurant: restaurant['price'] == 1, restaurants))
