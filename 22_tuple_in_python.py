def create_student():
    return 'Hasitha', 1992, 'Sri lanka'


stu = create_student()

# tuple destructing
name, bd, country = stu

print(stu)
print(name)
print(bd)
print(country)

# List vs Tuple
# tuple is more efficient since they are immutable
