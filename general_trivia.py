##TUPLES
A tuple is an immutable sequence of Python objects. Tuples are sequences, just like lists. 
The differences between tuples and lists are, the tuples cannot be changed unlike lists 
and tuples use parentheses, whereas lists use square brackets.

Creating a tuple is as simple as putting different comma-separated values.
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

The empty tuple is written as two parentheses containing nothing −
tup1 = ();
To write a tuple containing a single value you have to include a comma, even though there is only one value −
tup1 = (50,);

Like string indices, tuple indices start at 0, and they can be sliced, concatenated, and so on.


Accessing Values:
To access values in tuple, use the square brackets for slicing along with the index or indices to obtain value available at that index.
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print("tup1[0]: ", tup1[0])  //tup1[0]:  physics
print("tup2[1:5]: ", tup2[1:5]) //tup2[1:5]:  [2, 3, 4, 5]

Updating Tuples:
Tuples are immutable which means you cannot update or change the values of tuple elements. 
You are able to take portions of existing tuples to create new tuples

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)