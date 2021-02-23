import string;

# Numeric -> int & float
# boolean -> True , False
# String -> str
# number1 / number2 -> gives float result
# number1 // number2 -> gives result of integer division
# No pre increment & post increment operators like java.So you need to use usual way number1 +=1 or number1=number1+1
# logical operators -> and ,or, not, ^
# comparison operators exactly same as Java


# Python INT,FLOAT,BOOLEAN,STRINGS are immutable

# There are no char data type in python.So every thing behave like string.
# Internally it works as char array.So we could loop like below

message = 'Hello Hasitha'
for ch in message:
    print(ch)

# Check something inside , use 'in' (similar to contains in Java).This is substring chek
print('abc' in string.ascii_letters)
