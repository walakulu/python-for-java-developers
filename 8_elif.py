x_string = input("Enter a number :")
number = int(x_string)

if number == 1:
    print(f'number is {number}')
    print('This part of if statement')

elif number == 2:
    print(f'number is {number}')
    print('This part of elif statement')

else:
    print(f'number is {number}')
    print('This part of else statement')

# we can pass any values to if condition (unlike java)

if 5:
    print('Hello')

# Integer 0 , Float 0.0, Empty string return False  -> bool(anything)
# all other things return true
