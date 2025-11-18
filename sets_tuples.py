#Sets and tuples examples:
set1 = {1, 2, 3, 4, 5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

set2={"apple", "banana", "cherry", "cherry"}
print(set2)
#Tuples can't be changed after creation; making it useful for storing data that can't be modified.
#tuples examples:
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))
social_security_num = (12344, 4444445, 5676789)
print(social_security_num)