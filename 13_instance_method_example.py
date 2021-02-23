class Book:

    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.copies))

    def increase_no_of_copies(self, number_of_copies):
        self.copies = self.copies + number_of_copies
        return self.copies

    def decrease_no_of_copies(self, number_of_copies):
        self.copies = self.copies - number_of_copies
        return self.copies


book1 = Book('Harry Porter', 10)
print(book1)
book1.increase_no_of_copies(5)
print(book1)
book1.decrease_no_of_copies(10)
print(book1)

# Note: Python object is a hashmap of key value pair.We could add attribute to abject at runtime
# Ex book1.likes=10   //this will add like attribute to book object
# Python hopes programmers to behave politely.
