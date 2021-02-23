class Person:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)


# we are inheriting person class
class Student(Person):

    def __init__(self, name, grade):
        # initialize super class constructor
        super().__init__(name)
        self.grade = grade

    def __repr__(self):
        return repr((super().__repr__(), self.grade))


student1 = Student('Hasitha', 12)

print(student1)