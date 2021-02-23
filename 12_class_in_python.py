# The name we give to file is called 'Module name'.We could define multiple modules inside a single module

"""
Create empty class name Glass and create two objects

<__main__.Glass object at 0x7fc0a7fa1040>
<__main__.Glass object at 0x7fc0a7eb0400>
"""


class Glass:
    # pass -means nothing
    pass


glass1 = Glass()
glass2 = Glass()
print(glass1)
print(glass2)


# -----------------------------------------------------------------
# we cannot have overloaded constructors or methods.If we need , we have to use default values for arguments

class Book:
    # constructor
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    # this is similar to toString in java
    def __repr__(self):
        # need to pass a tuple
        return repr((self.name, self.copies))


# by default python pass 'self' for each method (including constructor)
book1 = Book('Harry Porter', 5)
print(book1)
