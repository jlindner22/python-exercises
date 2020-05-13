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

friends = {'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons': 10}
print(friends['no_of_seasons']) #10

##adding a key
friends['no_of_episodes'] = 236
friends['best_episode'] = 'The One With The Cake'

##delete a key value pair
del friends['best_episode']
print(friends)

friends['creators'] = ['David Crane', 'Marta Kauffman']

