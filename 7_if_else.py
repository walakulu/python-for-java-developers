number = 5

if number % 2 == 0:
    isEven = True
else:
    isEven = False

print(isEven)

# shortcut way
isEven = True if number % 2 == 0 else False
print(isEven)

isEven = 'Yes' if number % 2 == 0 else 'No'
print(isEven)
