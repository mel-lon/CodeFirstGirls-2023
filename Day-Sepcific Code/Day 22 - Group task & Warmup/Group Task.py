# It is the CFG Degree graduation day and you are a photographer who has the task to take photos of
# our graduates. The overall group has an even number of students, but Software graduates wear purple
# mortarboard hats and Data graduates wear black mortarboard hats. In fact, exactly half of all students
# has purple hats and the other half has black ones.
# We need to arrange our students in two rows before taking any photos. Each row must contain the
# same number of students and follow these precise guidelines:


def graduation_check(black,purple):
    black.sort()
    purple.sort()
# • All Software students with purple hats must be in the same row.
# • All Data students with black hats must be in the same row.


    first_row_colour = "PURPLE" if purple[0] < black[0] else "BLACK"
# • Each student in the back row must be strictly taller than a student directly in front of them in
# the front row.


# NB: you can assume that the overall group has at least two students.


# We are given two input arrays:
# • One contains the heights of all the students with purple hats
# • Another one contains heights of all the students with black hats.


    for idx in range(len(purple)):
        purple_height = purple[idx]
        black_height = black[idx]


# NB: these arrays will always be the same length and each height (number) will be a positive integer.
# Please write a function that returns whether or not a graduation photo that follows the above strict
# guidelines can be taken.

        if first_row_colour == 'PURPLE':
            if purple_height >= black_height:
                return False
        else:
            if black_height >= purple_height:
                return False
    return True

