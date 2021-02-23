# print once
print('Hello world')


# print twice
# python support structural programming.When we define methods outside of class ,
# we don't need to make them static like java does.
# make sure to keep proper indentations
# method start with lowercase as best practice
def print_hello_world_twice():
    print('Hello world 1')
    print('Hello world 2')


print_hello_world_twice()


# no need to define data type
def print_hello_hasitha_multiple_times(times):
    for i in range(1, times + 1):
        print('Hello Hasitha')

    # we could write in single time.But that is bad practice (PEP8)
    # for i in range(1, times + 1): print('Hello Hasitha')


print_hello_hasitha_multiple_times(4)
