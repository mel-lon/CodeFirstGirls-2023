# You are tasked with calculating the minimum classes we
# need to have so we know how many people to employ.
# Write a function which when given a number of students, calculates and prints
# out a string for your proposed number of classes, and a dictionary showing the allocation.
# Key Constraints:
# ●	The maximum size of a class is 30
# ●	There needs to be a minimum of 2 classes
# ●	The distribution of each class should be as even as possible.
# ●	We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!

def minimum_classes_calculator(students):
    if students < 2:
        raise ValueError("You need enough students to put them in more than one class")


    #### Calculating the minimum number of classes in each class
    minimum_number_of_classes = (students - 1) // 30 +1 # float error with /

    #### calculating the size of each class itself
    size_of_each_class = students // minimum_number_of_classes

    #### calculat4e the classes which may have an additional student
    surplus_classes = students % minimum_number_of_classes

    ########putting students into their respective classes
    class_order = {}
    remainder = students

    for student in range(minimum_number_of_classes):
        size = size_of_each_class + (student < surplus_classes)

        class_order[f'Class {student+1} '] = size

        remainder -= size

    print(f"The minimum number of classes you need is {minimum_number_of_classes}")
    for k, v in class_order.items():
        print(f"{k}: {v} students")

print(minimum_classes_calculator(100))