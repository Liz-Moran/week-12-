# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.


#collections are used to store multiple items in a single variablr
#lists are ordered collections of items
#lists are mutable, you can change their content
#lists are created using squre brackets[]

#Instead of making a bunch of seperate variables, you can store them in a list to make our job easier when you need to manage a bunch of items 
my_list1=[1, 2, 3, 4, 5,]
print(my_list1) 
print(type(my_list1))
print(my_list1[0]) 
print(my_list1[1:4])
print(my_list1[0:])
print(my_list1[0:-1])

my_list1.append(6)
print(my_list1)

my_list1.append(7)
print(my_list1)
my_list1.append(8)
print(my_list1)

my_list1.extend([10, 11, 12, 13, 14])
print(my_list1)

my_list1.extend(list(range(15, 515)))
print(my_list1)

my_list1.extend(list(range(515,1115 )))
print(my_list1)
# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
fav_foods = ['Tamales', 'Pozole', 'Pizza', 'Tacos', 'Chicken']
# Print the second and last item.
print(fav_foods[1])
print(fav_foods[4])
# Add a new item using .append().
fav_foods.append('Cheesecake')
print(fav_foods)
# Remove the first item using .pop(0).
fav_foods.pop(0)
print(fav_foods)
# Reverse your list using .reverse().
fav_foods.reverse()
# Create a list of 3 lists (matrix), and access the middle element.
