# classes_objects.py
# Basic class and object example

class Student:
    # class variable
    school_name = "ABC School"

    # method
    def display_info(self, name, age):
        print("Name:", name)
        print("Age:", age)
        print("School:", Student.school_name)


# Creating object
s1 = Student()
s1.display_info("Madhav", 20)