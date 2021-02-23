# All python exceptions are unchecked
# Ex: AttributeError - when try to access non existing method or attribute
# to get full exception list , run this in command shell ( it will show the exception hierarchy)
import builtins

# help(builtins)

# ------------------------ EXCEPTION HANDLING--------

try:
    i = 0
    number = 10 / i
# except(ZeroDivisionError, ValueError):
except ZeroDivisionError as err:
    print(err) # log the error
    number = 10
else:
    print('else')  # this will execute when exception not thrown
finally:
    print('Always execute')

print(number)
