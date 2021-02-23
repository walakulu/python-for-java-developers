# This is key value pair like java hash map


dict1 = dict(a=3, b=10, c=5)
print(dict1)

# print value of b(key b)
print(dict1['b'])

# KeyError , since no key name like e
# print(dict1['e'])

# Above situation could overcome using below
# Print None
print(dict1.get('e'))

# Print default value given
print(dict1.get('e', 'Error'))

# return keys
print(dict1.keys())
# Return values
print(dict1.values())
# return items (return tuples)
print(dict1.items())

# print key and value
for (key, val) in dict1.items():
    print(f'{key} {val}')
