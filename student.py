"""
Cara Krug 11/1/2020 cjkrug@dmacc.edu
Write unit tests to test the Student class:
Include setUp() and tearDown() methods
Write unit test test_object_created_all_attributes(self)
Write unit test test_student_str(self) etc..
"""
class Student:
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        if not (isinstance(gpa, float)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

