marks = [56, 70, 44]

print(sum(marks))
print(max(marks))
print(len(marks))

# add an specific item to list
marks.append(80)
print(marks)
marks.insert(3, 77)
print(marks)

# add an array of items
marks.extend([59, 80])
print(marks)

# remove 1st item which equals to 80
marks.remove(80)
print(marks)

# delete item in specific index
del marks[2]
print(marks)

# NOTE: No restriction on type of element which could contain in the list.You could have anything in the list.

# Here also have IndexError when access out of bound items.
