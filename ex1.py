#4
# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car, "in each car.")


#5
# name = 'Zed A. Shaw'
# age = 35
# height = 74
# weight = 180
# eyes = 'Blue'
# teeth = 'White'
# hair = 'Brown'

# print(f"Let's talk about {name}.")
# print(f"He's {height} inches tall.")
# print(f"He's {weight} pounds heavy.")
# print("Actually that's not too heavy.")
# print(f"He's got {eyes} eyes and {hair} hair.")
# print(f"His teeth are usually {teeth} depending on the coffee")

# total = age + height + weight
# print(f"If I add {age}, {height}, and {weight} I get {total}.")

# print(round(9.2323))

#6
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)