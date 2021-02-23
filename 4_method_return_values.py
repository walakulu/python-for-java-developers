# we do not need to mention return type.If we return some value it will print.
# If we don't print , it will return inbuilt "None" value
def sum_of_two_numbers(first_number, second_number):
    result = first_number + second_number;
    return result


print(sum_of_two_numbers(10, 30))


def sum_of_two_numbers_foget_return(first_number, second_number):
    result = first_number + second_number


# this will print None (instance of python default None class)
print(sum_of_two_numbers_foget_return(40, 60))
