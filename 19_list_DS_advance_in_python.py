from operator import attrgetter

# SLICING
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
# ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
print(numbers)

# print numbers from  index 2 to 6
# ['Two', 'Three', 'Four', 'Five']
print(numbers[2:6])

# print numbers form 0 to 6th index
# ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
print(numbers[:6])

# print numbers from 6th index to end of the list
# 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
print(numbers[6:])

# print numbers in every 2nd element (start from index 1 end end in index 8)
# ['One', 'Three', 'Five', 'Seven']
print(numbers[1:8:2])

# print numbers in every 3rd element (apply for whole list)
# 'Zero', 'Three', 'Six', 'Nine']
print(numbers[::3])

# print numbers in every 3rd element  in reverse order(apply for whole list)
# ['Ten', 'Seven', 'Four', 'One']
print(numbers[::-3])

# Delete numbers from index 5 to 7 (not include 7)
# ['Zero', 'One', 'Two', 'Three', 'Four', 'Seven', 'Eight', 'Nine', 'Ten']
del numbers[5:7]
print(numbers)

# Replace One ,Two with their corresponding numerics
# ['Zero', 'One', 'Two', 'Three', 'Four', 'Seven', 'Eight', 'Nine', 'Ten']
# ['Zero', 1, 2, 'Three', 'Four', 'Seven', 'Eight', 'Nine', 'Ten']
numbers[1:3] = [1, 2]
print(numbers)

# ---------------------------------------- REVERSE LIST
int_numbers = [1, 2, 5, 7, 2, 3]
# This is inplace reverse
int_numbers.reverse()

# If we need to access items while reversing
# this will return a iterator (original list will never modify)
for item in reversed(int_numbers):
    print(item)

# --------------------------------------SORTING

# Inplace sort
int_numbers.sort()

# Sorted return an iterator (original list will never modify)
for item in sorted(int_numbers):
    print(item)

# sort based on specified characteristic and reverse
string_num = ['One', 'Two', 'Three']
for item in sorted(string_num, key=len, reverse=True):
    print(item)


# ----------------------------------- APPLY OPERATION TO CUSTOM CLASSES

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return repr((self.name, self.age))


students = [Student('Hasitha', 28), Student('Ruwan', 25), Student('Mahesh', 27)]
# Error.Since python does not know which attribute to use for sort
# print(students.sort())

# sort by age
students.sort(key=attrgetter('age'))
print(students)

# --------------------------------------- LIST COMPREHENSION


fruits = ['Banana', 'Apple', 'Orange', 'Mango', 'Guava']
# number length of each item
number_length_arr=[len(fruit) for fruit in fruits]
print(number_length_arr)

# convert fruits into upper
fruits_in_upper_case=[fruit.upper() for fruit in fruits]
print(fruits_in_upper_case)

# print fruits have five letters

length_five_fruits = []
for fruit in fruits:
    if len(fruit) == 5:
        length_five_fruits.append(fruit)

print(length_five_fruits)

# Above thing could be done with list comprehension with easily
fruit_lengths_five=[fruit for fruit in fruits if len(fruit)==5]
print(fruit_lengths_five)