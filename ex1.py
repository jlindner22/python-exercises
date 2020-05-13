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

# #6
# types_of_people = 10
# x = f"There are {types_of_people} types of people."

# binary = "binary"
# do_not = "don't"
# y = f"Those who know {binary} and those who {do_not}."

# print(x)
# print(y)

# print(f"I said: {x}")
# print(f"I also said: '{y}'")

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! {}"

# print(joke_evaluation.format(hilarious))

# w = "This is the left side of..."
# e = "a string with a right side."

# print(w + e)

# #7
# print("Mary had a little lamb.")
# print("Its fleece was white as {}.".format('snow'))
# print("And everywhere that Mary went.")
# print("." * 10)

# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"

# #end = ' ' allows for printing without a new line
# print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# print(end7 + end8 + end9 + end10 + end11 + end12)

#8
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Roses are red", "Violets are blue", "You're reading my repo", "and I did that too."
))


