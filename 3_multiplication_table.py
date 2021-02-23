def print_multiply_table(multiplier=5, from_number=1, to_number=10):
    for i in range(from_number, to_number + 1):
        print(f'{multiplier} x {i} = {multiplier * i}')


# by default , print multiplication table for 5
print_multiply_table()

# print multiplication table for 6
print_multiply_table(6)

# print multiplication table for 7. (multiply should include 31 to 40
print_multiply_table(7, 31, 40)


# --------------------------------------------------------------------------------------------------
# NOTE : PYTHON DOES NOT SUPPORT TO METHOD OVERLOADING.WE CAN HAVE ONLY ONE METHOD WITH SAME METHOD NAME
# If we put two methods with different signatures, python automatically overwrite 1st method with second method
# some bad example are below
def print_multiply_table(multiplier):
    print_multiply_table(multiplier, 1, 20)

# gives error.Since we have overwritten the previous 3 argument method by above single argument method
# print_multiply_table(5)
