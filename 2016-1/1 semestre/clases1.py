class Student(object):
    name = ""

    def __init__(self, name):
        self.name = name


def make_student(name):
    student = Student(name)
    return student
