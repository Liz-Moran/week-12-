# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

#score calculator
score= int(input("Enter your score (0-100): "))
#if score is between 90 and 100 then assign grade A
if 90 <= score <= 100:
    print("Grade: A")
#if score is between 80-89 then assign grade B
elif 80 <=score <=89:
    print("Grade: B")
#if score is bewteen 70-79 then assign grade C
elif 70 <= score <=79:
    print("Grade C: ")
#if score is between 60-69 then assign grade D
elif 60 <= score <= 69:
    print("Grade: D")
#if score is between 50-59 then assign grade F
elif 50 <= score <=59:
    print("Grade: F")


# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
p= int(input("Enter a number: "))
print(50<=p<=100)
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
y= int(input("Enter a number: "))
print(not(y==0) and (y>10))
# Use chained comparison to check if 3 < 4 < 5.
a=3
b=4
c=5
print(a<b<c)
# Challenge: Create a password rule using logical operators:
password = input("Enter your password: ")
if len(password) >= 4 and any(char.isdigit() for char in password):
    print("Password is valid.")
else: 
    print("Password is invalid.")
