list1=[1,2,3]
list2=[4,5,6]
nested_list = [list1, list2]
print(nested_list)
print(nested_list [0][2])



groceries = [["apple" ,"orange", "banana", "coconut"],
             ["celery","carots","potatos"],
             [ "chicken", "fish", "turkey"]]

for collection in groceries:
   print(collection)
   for food in collection:
     print(food, end=" ")
     print()
   

num_pad= ((1, 2, 3), (4,5,6), (7,8,9,), ("*", 0,"#"))
for row in num_pad:
   for num in row:
     print(num, end = " ")
     print()


# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#List comprehension
print(matrix[1][2])    # 6
print(matrix[0][2])
print(matrix[0][0])
example_list = [row[0] for row in matrix]
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:
matrix = [
   [10, 20, 30],
   [40, 50, 60],
   [70, 80, 90]
]


# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.
print(matrix[0])
# Print the second item from the third list.
print(matrix[2][1])
# Use a list comprehension to extract the last item from each sub-list.
mat_list = [row[2] for row in matrix]
print(mat_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.

squared_numbers = [x**2 for x in range(1, 11)]
for x in range(1,11):
   squared = x**2
   print(squared)