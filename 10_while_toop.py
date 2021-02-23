# Python support break; and continue ; exactly like java

i = 0

while i < 11:
    print(i)
    i += 1

# print all the squares of number < 200

"""
We could not use 'for' because we need to give loop count(range(1, 1000)) from the beginning
"""
# def print_squares_less_than(threshold):
#     for i in range(1, 1000):
#         square_of_number = pow(i, 2)
#         if square_of_number < threshold:
#             print(square_of_number)
#
#
# print_squares_less_than(200)


"""
We could write above code using 'while' without requiring loop count
"""


def print_squares_less_than(threshold):
    i = 1
    while i * i < threshold:
        print(i * i)
        i += 1


print_squares_less_than(100)
